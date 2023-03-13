import requests
import re
from bs4 import BeautifulSoup

# Get the link of the website
req = requests.get("https://www.google.com/finance/quote/USD-CNY?sa=X&ved=2ahUKEwiD3_b04df9AhU6FzQIHdXoDpcQmY0JegQIBhAd")

# Web scraper tool
soup = BeautifulSoup(req.content, "html.parser")

# First get the text of the web page, then split the strings with ""
text = soup.get_text().split()


# Requirement of keyword
pattern = re.compile(r'^CNY(\d+\.\d+)Mar')

# For loop to find the specific string satifies the pattern
for string in text:
    match = pattern.search(string)
    if match:
        var = match.group(1)
        print(var)
