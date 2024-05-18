# This file is for backend main interaction
from flask import Flask, jsonify, request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from dataExtraction import getStocks



app = Flask(__name__)





# Getting stocks that meet a certain criteria described in the 
@app.route('/stocks', methods=['GET'])
def get_stocks():
    peRatio = request.args.get('peRatio')
    sector = request.args.get('sector')
    if peRatio is None or sector is None:
        return jsonify({'error': 'Please provide both peRatio and sector as query parameters'}), 400
    stocks = getStocks(peRatio, sector)
    return jsonify({'stocks': stocks})






app.run()
