from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import requests,time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.page_load_strategy = 'eager'
# options.add_argument("--incognito")
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

def openURL(urlOpen):
    req = Request(urlOpen, headers=HEADERS)
    webpage = urlopen(req).read()
    return soup(webpage, "html.parser")
# options.add_argument('--headless=new')
# driver = webdriver.Chrome( options=options)

# Gather all stocks that matches specific criteria 
# In the future we can change this
# We can then specify the different things needed for this stock
# peRatio = 15
# sector = 'technology'
# url = "https://finviz.com/screener.ashx?v=111&f=fa_pe_u"+str(peRatio)+",fa_salesqoq_high,sec_"+sector+"&ft=2"
# req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# html = soup(webpage, "html.parser")
# allStocks = []
# for a in html.select("tr#screener-table a.tab-link"):
#     allStocks.append(a.text)



# https://www.investing.com/news/stock-market-news/earnings-call-axcelis-technologies-reports-strong-q3-2023-results-bullish-on-silicon-carbide-market-93CH-3220157
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

# Researching what the news of the stock say 
# Going into article page
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
# getArticles('Axcelis','ACLS',2)
articleContent('https://www.investing.com/news/stock-market-news/earnings-call-axcelis-technologies-reports-strong-q3-2023-results-bullish-on-silicon-carbide-market-93CH-3220157')
# print(html)
# /html/body/div[6]/section/div[5]/p[10]
# #leftColumn > div.WYSIWYG.articlePage > p:nth-child(4)




# webpage = urlopen(req).read()
# html = soup(webpage, "html.parser")
# print(ht)
# print(html)
# Result = searching.find_element(By.CSS_SELECTOR, 'span.mr-3')

# html = soup(driver.page_source, 'lxml')





# driver.get(url)

# driver.find_element(By.CSS_SELECTOR, 'button[id="onetrust-accept-btn-handler"]').click()

# driver.find_element(By.CSS_SELECTOR, 'a.js-inner-all-results-quote-item').click()
# driver.get(driver.current_url+'-news')

# article = driver.find_elements(By.CSS_SELECTOR, 'article')
#     # print(article.get_attribute('href'))
# print(article)
# <a class="js-inner-all-results-quote-item row" href="/equities/symantec-corp">
# <span class="flag first"><i class="ceFlags middle USA"></i></span>
# <span class="second">GEN</span>
# <span class="third">Gen Digital Inc</span>
# <span class="fourth">Stock - NASDAQ equities</span>
# </a>

