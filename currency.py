import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime

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


def ask():
    print("####### New Program #######")
    # Get the latest date and time
    now = datetime.now()
    time = now.strftime("%m/%d/%Y %H:%M:%S")
    print("Currency: " + str(var) + "\n" + time + "\n")
    #"""
    choice = int(input("'1' start with latest ratio, '2' use different ratio:, '3' to exit: "))
    if choice == 1:
        calculate()
    elif choice == 2:
        calculate2()
    else:
        return

def calculate():
    way = int(input("'1': rmb -> usd, '2': usd -> rmb: "))
    ratio = var
    amount = input("Enter the amount: ")
    if way == 1:
        print("Current ratio: " + var)
        print("Amount of $:", round((float(amount) / float(ratio)), 4))
        print("\n")
        print("\n")
    elif way == 2:
        print("Current ratio: " + var)
        print("Amount of ¥:", round((float(amount) * float(ratio)), 4))
        print("\n")
        print("\n")
    ask()

def calculate2():
    way = int(input("'1': rmb -> usd, '2': usd -> rmb: "))
    ratio = input("Enter the ratio: ")
    amount = input("Enter the amount: ")
    if way == 1:
        print("Amount of $:", round((float(amount) / float(ratio)), 4))
        print("\n")
        print("\n")
    elif way == 2:
        print("Amount of ¥:", round((float(amount) * float(ratio)), 4))
        print("\n")
        print("\n")
    ask()


ask()
