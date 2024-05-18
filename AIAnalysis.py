from DataExtraction import openURL, articleContent
from News import AnalysedArticle
import requests

# The AI stock analysis part

# Hugging Face API setup
API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# This does it for one article only
def analyseData(article):
    # Get the article content
    contents = articleContent(article)

    # Check if the article content was successfully retrieved
    if not contents:
        print("No content retrieved from the article.")
        return
    
    # Send the content to the Hugging Face API for analysis
    output = query({
        "inputs": contents
    })
    
    # Print the API response for debugging purposes
    # print("API response:", output)
    
    # Check if the response contains the expected data
    if not isinstance(output, list) or not all(isinstance(item, list) for item in output):
        print(output)
        print("Unexpected API response format.")
        return

    stockAnalysed = AnalysedArticle(newsLink=article)

    try:
        # Add the paragaph 
        for item in contents:
            stockAnalysed.add_paragaph(item)

        # Process the response to extract scores
        for item in output:
            for label_score in item:
                stockAnalysed.add_score(label_score['label'], label_score['score'])

        # Print all the positive and negative scores
       
        # stockAnalysed.print_arrays();
      
        
        

        # # Print the average scores
        # print("Average Positive Score:", stockAnalysed.average_positive())
        # print("Average Negative Score:", stockAnalysed.average_negative())
        # stockAnalysed.print_most_negative();
        # stockAnalysed.print_most_positive();
        
        # print("-----")
        # print("-----")
        return stockAnalysed

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the analyseData function with a sample link
analyseData('https://www.investing.com/news/stock-market-news/earnings-call-acm-research-posts-robust-q1-earnings-targets-global-expansion-93CH-3432366')
