#!/usr/bin/env python3 

import urllib.request
import requests 
import json 


# getting api key from file 

with open("/home/student/alpha.creds") as mycreds:
    alpha_creds = mycreds.read()


alpha_creds = "apikey=" + alpha_creds.strip("\n")




# capturing "symbol" variable
print("\nAPI function=TIME_SERIES_INTRADAY\n")
print("Provide the symbol of the equity of your choice.") 
print("For example: symbol=IBM")
print("=================================================================")
symbol = input("\nsymbol=").upper()



while len(symbol) > 4:
    print("\nInvalid symbol. Try again.")
    symbol = input("\nsymbol=")
    if len(symbol) < 4:
        break
     



# capturing "interval" variable 
print("\nTime interval between two consecutive data points in the time series.")
print("The following values are supported (in minutes):")   
print("1, 5, 15, 30, 60")
print("=================================================================")
interval = int(input(">>>"))
#while true: 
    #if interval != 1, 5, 15, 30, 60:
        #print("Unsupported value. Try again.")
        #interval = input(">>>")

supported = [1, 5, 15, 30, 60]

while interval not in supported:
    print("\nUnsupported value, try again.")
    interval = int(input(">>>"))
    if interval in supported:
        break

     


# getting intraday data from user input (above) in JSON format 
## calling api
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}min&'+ alpha_creds
## requesting data
r = requests.get(url)
## reading data as JSON 
data = r.json()


# getting specified json key
key = data.get(f"Time Series ({interval}min)")

# displaying values from specified json key 
for values in key:
    print (values)






"""
# printing income statement data 
url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&{alpha_creds}'
r = requests.get(url)
data = r.json()

for net in data["results"]:
    print(data.get("netIncome"))
"""

