#!/usr/bin/env python3 

"""A script that calls time series closing value data from the Alpha Vantage API database. Closing values and the overall average value will be displayed. Data will then be saved in a file if desired. | wilmerdanny@icloud.com"""

import requests 
import json 
import datetime 


# getting api key from file 


with open("/home/student/alpha.creds") as mycreds:
    alpha_creds = mycreds.read()


alpha_creds = "apikey=" + alpha_creds.strip("\n")



now = datetime.datetime.now()
print(now)
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
print("\nEnter desired time interval between two consecutive data points in the time series.")
print("The following values are supported (in minutes):")   
print("1, 5, 15, 30, 60")
print("=================================================================")
interval = int(input(">>>"))

## if "interval" input is not compatible, loop until it is 
supported = [1, 5, 15, 30, 60]
while interval not in supported:
    print("\nUnsupported value, try again.")
    interval = int(input(">>>"))
    if interval in supported:
        break


# getting intraday data from user input (above) in JSON format 
## calling api
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}min&{alpha_creds}'
## requesting data
r = requests.get(url)
## reading data as JSON 
data = r.json()


# getting specified json key
key = data.get(f"Time Series ({interval}min)")

# displaying values from specified json key

prices = []
for ts in key:
    high_price = data[f'Time Series ({interval}min)'][ts]['2. high']
    print(ts, high_price)
    prices.append(float(high_price))

#print(prices)
print("\nAverage:")
print(sum(prices)/len(prices))

#print(json.dumps(data))

