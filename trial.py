from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# URL of the page
url = "https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_pe_u10,sec_technology&ft=2"

# Create a request object
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# Open the URL and read the HTML content
webpage = urlopen(req).read()

# Parse the HTML content
page_soup = soup(webpage, "html.parser")

# Find all elements with valign="top"
valign_top_elements = page_soup.find_all(valign="top")

# Select the third td within each valign="top" element
for element in valign_top_elements:
    td_elements = element.find_all("td")
    if len(td_elements) >= 3:  # Ensure at least 3 td elements exist
        first_td = td_elements[1].text.strip()
        third_td = td_elements[2].text.strip()
        print(third_td)
        print(first_td)
