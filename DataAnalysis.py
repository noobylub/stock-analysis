# This is where I will be putting the analysis
# Gathering all the data and reporting the main points. 
from DataExtraction import getStocks, getArticles
from AIAnalysis import analyseData

# Analyse the data from here
# Average of all both positive and negative
# Get the most three negative and positive articles
def stockAnalysis(stockName, stockTicker):
    allArticles = getArticles(stockName,stockTicker);
    # print(allArticles)
    ArticleAnalysed = []
    for article in allArticles:
        dataAnalysed = analyseData(article)
        ArticleAnalysed.append(dataAnalysed);
    # print (allArticles);
    total_positive_scores = []
    total_negative_scores = []
    
    for art in ArticleAnalysed:
       
        total_positive_scores.extend(art.positive_scores)
        total_negative_scores.extend(art.negative_scores)

    average_positive = sum(total_positive_scores) / len(total_positive_scores) if total_positive_scores else 0
    average_negative = sum(total_negative_scores) / len(total_negative_scores) if total_negative_scores else 0
    print("---")
    print("---->>>")
   
    print(average_negative)
    print(average_positive)





stockInfo = getStocks(12, 'technology')[1];
stockAnalysis(stockInfo[1], stockInfo[0])


