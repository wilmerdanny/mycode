#!/usr/bin/env python3 

"""A script that calls time series closing value data from the Alpha Vantage API database. Closing values and the overall average value will be displayed. Data will then be saved in a file if desired. | wilmerdanny@icloud.com"""

import requests 
import json 
import datetime 
import os

# predefining paths

creds_path  = "/home/student/alpha.creds"


# getting api key from file 

def get_symbol():

    # capturing "symbol" variable
    print("\nAPI function=TIME_SERIES_INTRADAY\n")
    print("Provide the symbol of the equity of your choice.") 
    print("For example: symbol=IBM")
    print("=================================================================")

           
    symbol = input("symbol=").upper()
    while len(symbol) > 4:
        print("\nInvalid symbol. Try again.")
        symbol = input("symbol=").upper()
    else:
        return symbol


def get_interval():

    # getting interval 

    print("\nEnter desired time interval between two consecutive data points in the time series.")
    print("The following values are supported (in minutes):")   
    print("1, 5, 15, 30, 60")
    print("=================================================================")

    interval = int(input(">>>"))
    # small check to help catch compatibility issues 
    supported = [1, 5, 15, 30, 60]
    while interval not in supported:
        print("\nUnsupported value, try again.")
        interval = int(input(">>>"))
    return interval


def get_api():
    # getting apikey
    with open("/home/student/alpha.creds") as mycreds:
        alpha_creds = mycreds.read()
        apikey = "apikey=" + alpha_creds.strip("\n")
        return apikey


cont = input("Continue? Y/n").lower()
while cont == "y":
    cont = input("Continue? Y/n").lower()

    symbol = get_symbol()
    print(symbol)

    interval = get_interval()
    print(interval)

    alpha_creds = get_api()
    print(alpha_creds)






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

    print("\nAverage:")
    average = (sum(prices)/len(prices))
    print(average)


    save_or_not = input("Would you like to save output as file? Y/n").lower()
    if save_or_not == "y":
        # saving output to file 
        contents = f"PRICES\n======\n{str(prices)}\nAVERAGE\n=======\n{str(average)}"
        save_path = f"/home/student/mycode/project/intraday_storage/{symbol}_{str(datetime.datetime.now())}" 
        with open(save_path, "w") as fp:
            fp.write(contents)
            pass 

        print(f"\nDone! output saved in file here:\n{save_path}")
    else:
        print("Ok. No file has been saved.")


