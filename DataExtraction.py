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

    valign_top_elements = html.find_all(valign="top")
    # Select the third td within each valign="top" element
    for element in valign_top_elements:
        td_elements = element.find_all("td")
        if len(td_elements) >= 3:  # Ensure at least 3 td elements exist
            companyTicker = td_elements[1].text.strip()
            companyName = td_elements[2].text.strip().split(' ')[0]
            allStocks.append((companyTicker,companyName))
            
   
    return allStocks
print("stock list")
# We can just output  5 stocks
print(getStocks(12,'technology')[0])



# https://www.investing.com/news/stock-market-news/earnings-call-axcelis-technologies-reports-strong-q3-2023-results-bullish-on-silicon-carbide-market-93CH-3220157
# Get the content of the individual article
def articleContent(link):
    
    # Open the provided link and parse the HTML content
    html = openURL(link)
    
    # Select all paragraphs within the div with class 'WYSIWYG.articlePage'
    contents = html.select('#article > div > p')
   
    # List to store the cleaned text content of paragraphs
    goodContent = []
    
    # Loop through each paragraph
    for p in contents:
        # Get the text content of the paragraph, remove leading and trailing whitespaces
        goodContent.append(p.getText().strip(' '))
    
    # Remove empty strings from the list
    goodContent = [x for x in goodContent if x]
    # Limit the list to 10 elements if it exceeds 10
    if(len(goodContent) > 11):
        goodContent = goodContent[:10]

    # Print each paragraph separately
    # for p in goodContent:
    #     print("-----")
    #     print(p)
    return goodContent


# Call the articleContent function with a sample link
# print(articleContent('https://www.investing.com/news/stock-market-news/earnings-call-acm-research-posts-robust-q1-earnings-targets-global-expansion-93CH-3432366'))


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
            # check if article has the stock name and is not pro
            if(artContainName == True and artPro == False):
                linkToVisit.append(baseURL+ article['href'])

        # for article in linkToVisit:
        #     print(article)
        return linkToVisit;

# Combining the stocks you got and the articles of those stocks 
# def getAllArticles(peRatio, sector):
#     listofStocks = getStocks(peRatio, sector)
#     for companyTicker, companyName in listofStocks:
#         print("-------------------------")
#         print(companyName)
#         print(companyTicker)
#         getArticles(str(companyName),str(companyTicker),1)

    

# getArticles('ACM', 'ACMR',1)
# articleContent('https://www.investing.com/news/assorted/concentrix--webhelp-rebrands-as-concentrix-432SI-3389334')
# articleContent('https://www.investing.com/news/stock-market-news/earnings-call-axcelis-technologies-reports-strong-q3-2023-results-bullish-on-silicon-carbide-market-93CH-3220157')
# getAllArticles(10, 'technology')
# print("something")





