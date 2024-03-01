from flask import Flask, jsonify, request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# Initial setup for web scraping
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
def openURL(urlOpen):
    req = Request(urlOpen, headers=HEADERS)
    webpage = urlopen(req).read()
    return soup(webpage, "html.parser")

app = Flask(__name__)

usersList = ['Aaron', 'Bianca', 'Cat', 'Danny', 'Elena']

def getStocks(peRatio, sector):
    html = openURL("https://finviz.com/screener.ashx?v=111&f=fa_pe_u"+str(peRatio)+",fa_salesqoq_high,sec_"+sector+"&ft=2")
    allStocks = []
    for a in html.select("tr#screener-table a.tab-link"):
        allStocks.append(a.text)
    return allStocks

# Getting stocks that meet a certain criteria
@app.route('/stocks', methods=['GET'])
def get_stocks():
    peRatio = request.args.get('peRatio')
    sector = request.args.get('sector')
    if peRatio is None or sector is None:
        return jsonify({'error': 'Please provide both peRatio and sector as query parameters'}), 400
    stocks = getStocks(peRatio, sector)
    return jsonify({'stocks': stocks})



@app.route('/user/<int:id>', methods=['GET'])
def userById(id):
    return jsonify({ 'username': usersList[id]  })

@app.route('/user/<string:name>', methods=['GET'])
def getUserByName(name):
    # Show some user information
    return "Some info"

@app.route('/user/<string:name>', methods=['POST'])
def addUserByName(name):
    usersList.append(name)
    return jsonify({ 'message': 'New user added'  })

app.run()
