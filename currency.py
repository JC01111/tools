import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import datetime

# Get current date and time
now1 = datetime.datetime.now()
# Get current month's abbreviation
month_abbr = now1.strftime("%b")

# Get the link of the website
req = requests.get("https://www.google.com/finance/quote/USD-CNY?sa=X&ved=2ahUKEwiD3_b04df9AhU6FzQIHdXoDpcQmY0JegQIBhAd")
# Web scraper tool
soup = BeautifulSoup(req.content, "html.parser")
# First get the text of the web page, then split the strings with ""
text = soup.get_text().split()

# Requirement of keyword
pattern = re.compile(r'^CNY(\d+\.\d+)' + month_abbr)
# For loop to find the specific string satifies the pattern
for string in text:
    match = pattern.search(string)
    if match:
        var = match.group(1)


def ask():
    print("####### New Program #######")
    # Get the latest date and time
    now = datetime.datetime.now()
    time = now.strftime("%m/%d/%Y %H:%M:%S")
    print("USD to RMB: " + str(var) + "\n" + time + "\n" + "\n")
    # Ask for choice
    choice = int(input("'1' use latest ratio, '2' use different ratio, '3' exit: "))
    if choice == 1 or choice == 2:
        calculate(choice)
    elif choice == 3:
        return
    else:
        print("Invalid input")

def calculate(choice):
    if choice == 1:
        ratio = var
    else:
        ratio = float(input("Enter the ratio: "))
    # rmb->usd or usd to rmb
    way = int(input("'1': rmb -> usd, '2': usd -> rmb: "))
    if way == 1:
        amount = float(input("Enter the amount :¥ "))
        print("Amount of USD: $", round((float(amount) / float(ratio)), 4))
        print("\n")
        print("\n")
    elif way == 2:
        amount = float(input("Enter the amount :$ "))
        print("Amount of RMB: ¥", round((float(amount) * float(ratio)), 4))
        print("\n")
        print("\n")
    else:
        print("Invalid input")
    ask()

ask()
