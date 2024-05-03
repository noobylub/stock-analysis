from stockRecommend import openURL
import requests

# https://www.investing.com/news/stock-market-news/earnings-call-axcelis-technologies-reports-strong-q3-2023-results-bullish-on-silicon-carbide-market-93CH-3220157
# Get the content of the individual article
def articleContent(link):
    # Open the provided link and parse the HTML content
    html = openURL(link)
    
    # Select all paragraphs within the div with class 'WYSIWYG.articlePage'
    contents = html.select('div.WYSIWYG.articlePage > p')
    
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
totalArticle = articleContent('https://www.investing.com/news/stock-market-news/sealsq-introduces-quantumresistant-crypto-wallet-feature-93CH-3324951')





API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def analyseData(article):
    # Get the article and their score
    contents = articleContent(str(article))
    output = query({
	    "inputs": contents
    })
    # Keep track of positive and negative score
    positive_scores = []
    negative_scores = []
    for i in range(0,len(output)):
        for label_score in output[i]:
            if label_score['label'] == 'positive':
                positive_scores.append(label_score['score'])
            elif label_score['label'] == 'negative':
                negative_scores.append(label_score['score'])

    if positive_scores:
        avg_positive = sum(positive_scores) / len(positive_scores)
    else:
        avg_positive = 0

    # Calculate the average of negative scores
    if negative_scores:
        avg_negative = sum(negative_scores) / len(negative_scores)
    else:
        avg_negative = 0
    # All the positive score
    print("Positive Scores:", positive_scores)
    print("Negative Scores:", negative_scores)
    # print the average
    print("Average Positive Score:", avg_positive)
    print("Average Negative Score:", avg_negative)
    
	
# output = query({
# 	"inputs": articleContent('https://www.investing.com/news/stock-market-news/sealsq-introduces-quantumresistant-crypto-wallet-feature-93CH-3324951')
# })

output = analyseData('https://www.investing.com/news/stock-market-news/sealsq-introduces-quantumresistant-crypto-wallet-feature-93CH-3324951')


# for i in range(0,len(output)):
#     print(" ")
#     print(totalArticle[i])
#     print(output[i])




 