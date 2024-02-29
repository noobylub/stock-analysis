# from transformers import pipeline

# classification = pipeline('sentiment-analysis')
# classification(["I thoroughly enjoyed this movie!",
#                 "I did not understand anything in this movie."])

#  This is the 
import requests

API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": ['\xa0', 'Investing.com - Axcelis (NASDAQ: ACLS) reported second quarter EPS of $1.86, $0.36 better than the analyst estimate of $1.50. Revenue for the quarter came in at $274M versus the consensus estimate of $256.68M.', 'Axcelis sees Q3 2023 EPS of $1.72 versus the analyst consensus of $1.73.', 'Axcelis sees Q3 2023 revenue of $280.00M versus the analyst consensus of $260.70M.', 'Axcelis sees FY 2023 revenue of $1.10B versus the analyst consensus of $1.04B.', "Axcelis's stock price closed at $189.02. It is up 57.25% in the last 3 months and up 160.00% in the last 12 months.", "Axcelis saw 5 positive EPS revisions and 0 negative EPS revisions in the last 90 days. See Axcelis's stock price’s past reactions to earnings here.", 'According to InvestingPro, Axcelis\'s Financial Health score is "great performance".', "Check out Axcelis's recent earnings performance, and Axcelis's financials here.", "Stay up-to-date on all of the upcoming earnings reports by visiting Investing.com's earnings calendar"]
})
for i in output:
    print(" ")
    print(i)