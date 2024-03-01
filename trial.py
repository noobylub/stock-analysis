import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the article title
        title = soup.find('h1', class_='articleHeader').text.strip()
        
        # Find the article content
        content = soup.find('div', class_='WYSIWYG articlePage').text.strip()
        
        return title, content
    else:
        print("Failed to retrieve the article. Status code:", response.status_code)
        return None, None

# URL of the article
article_url = 'https://www.investing.com/news/assorted/axcelis-technologies-announces-additional-200m-share-buyback-432SI-3172542'

# Scrape the article
title, content = scrape_article(article_url)

# Print the title and content
if title and content:
    print("Title:", title)
    print("\nContent:", content)
else:
    print("Failed to retrieve the article.")
