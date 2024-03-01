from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup




HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
def openURL(urlOpen):
    req = Request(urlOpen, headers=HEADERS)
    webpage = urlopen(req).read()
    return soup(webpage, "html.parser")


# Gather all stocks that matches specific criteria 
# In the future we can change the parameters
# We can then specify the different things needed for this stock
def getStocks(peRatio, sector):
    html = openURL("https://finviz.com/screener.ashx?v=111&f=fa_pe_u"+str(peRatio)+",fa_salesqoq_high,sec_"+sector+"&ft=2")
    allStocks = []
    for a in html.select("tr#screener-table a.tab-link"):
        allStocks.append(a.text)
    return allStocks
print("stock list")
# We can just output  5 stocks
print(getStocks(12,'technology'))



# https://www.investing.com/news/stock-market-news/earnings-call-axcelis-technologies-reports-strong-q3-2023-results-bullish-on-silicon-carbide-market-93CH-3220157
# Get the content of the individual article
def articleContent(link):
    html = openURL(link)
    contents = html.select('div.WYSIWYG.articlePage > p')
    
    goodContent = []
    for p in contents:
        goodContent.append(p.getText().strip(' '))
    # print(goodContent)
    goodContent = [x for x in goodContent if x]
    if(len(goodContent) > 11):
        goodContent= goodContent[:10]
    print((goodContent))
# articleContent('https://www.investing.com/news/axcelis-earnings-beat-by-036-revenue-topped-estimates-3142440')
# Researching what the news of the stock say 
# Getting the articles and the links within them
def getArticles(name,ticker,page=2):
    # get to the search page and scrape the company news
    baseURL = 'https://www.investing.com'
    url = baseURL+'/search/?q='+ ticker
    html = openURL(url)
    url = html.find('a', class_ = "js-inner-all-results-quote-item row")['href']
    # You can specify how many pages of articles to scrape 
    for i in range(1,page+1):
        urlPlaceholder = baseURL+ url + '-news' + '/'+ str(i)
        # GET all the articles
        html = openURL(urlPlaceholder)
        linkToVisit = []
        for article in html.select('ul[data-test="news-list"] > li  a[href]'):
            artContainName = article['href'].lower().__contains__(name.lower())
            artPro = article['href'].lower().__contains__('pro')
            # print(artContainName, artPro)
            if(artContainName == True and artPro == False):
                linkToVisit.append(baseURL+ article['href'])
        for article in linkToVisit:
            print(article)
getArticles('Axcelis','ACLS',2)
articleContent('https://www.investing.com/news/assorted/axcelis-technologies-announces-cfo-change-432SI-3167573')
# articleContent('https://www.investing.com/news/stock-market-news/earnings-call-axcelis-technologies-reports-strong-q3-2023-results-bullish-on-silicon-carbide-market-93CH-3220157')






