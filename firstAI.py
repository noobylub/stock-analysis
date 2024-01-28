# from transformers import pipeline

# classification = pipeline('sentiment-analysis')
# classification(["I thoroughly enjoyed this movie!",
#                 "I did not understand anything in this movie."])

import requests

API_URL = "https://api-inference.huggingface.co/models/ProsusAI/finbert"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": ['Axcelis Technologies (NASDAQ:ACLS) Inc. has reported robust third-quarter 2023 earnings, surpassing its guidance with revenue of $292.3 million and earnings per share (EPS) of $1.99. The company also provided an optimistic outlook for the fourth quarter and the full year, with the power market, particularly silicon carbide, driving growth.', 'Key takeaways from the earnings call include:', "CEO Doug Lawson highlighted the company's growth prospects in the DRAM and silicon carbide markets during the earnings call. He stated that demand for DRAM is expected to rise, driven by factors such as AI servers, PC refresh cycles, and consumer demand. Lawson also noted the growing silicon carbide market, with 35% of the company's total system revenue coming from this segment.", "Lawson emphasized that the industry is transitioning from 150-millimeter to 200-millimeter wafers, and Axcelis' tools can be upgraded to accommodate this shift. He further discussed the potential for silicon carbide adoption in sectors beyond electric vehicles (EVs), including industrial markets, data centers, clean energy, smart grids, and communications applications.", 'In terms of geographical performance, the company noticed increased activity in China, despite some delays in the U.S. market. Axcelis also reported progress in the Japanese market, particularly within the power market and image sensor market. The company has been shipping silicon carbide tools to Japan and has observed a rising demand for power tools.', 'Axcelis is also focusing on penetrating the advanced logic market through R&D and has deployed evaluation and production systems. Lawson stressed the importance of reducing costs to expand into new markets. The company also announced upcoming investor events in November and December.', "In light of the recent earnings call, it's insightful to consider InvestingPro's data and tips. Axcelis Technologies, identified by the ticker ACLS, has shown some promising metrics. The company's adjusted market cap stands at $4200M USD, with a P/E ratio of 18.14. Over the last twelve months as of Q3 2023, Axcelis has achieved a revenue growth of 26.38%, indicating a strong financial performance.", 'InvestingPro tips shed light on a few key aspects of the company. Firstly, ACLS yields a high return on invested capital, an encouraging sign for potential investors. Secondly, it holds more cash than debt on its balance sheet, indicating a robust financial position. Lastly, ACLS has been consistently increasing its earnings per share, which is a positive sign for its financial health.', "For those interested in more detailed insights, InvestingPro offers additional tips and metrics. These include the company's performance, financial health, and market trends, among others. With InvestingPro, investors can stay informed and make well-rounded decisions.", 'Operator: Good day, ladies and gentlemen and welcome to the Axcelis Technologies Call to discuss the company’s results for the Third Quarter. My name is Corey, and I’ll be your coordinator today. [Operator Instructions] Please be advised that today’s conference call is being recorded. I would now like to hand the conference call over to your host for today’s call, Doug Lawson, Executive Vice President of Corporate Marketing and Strategy.'],
})
for i in output:
    print(" ")
    print(i)