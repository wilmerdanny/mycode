#!/usr/bin/env python3 

""" Description: 
    A script to interact with an 'open' API"""

# imports always go at the top of your code
import requests 


def main(): 
    # create resp, which is our request object 
    resp = requests.get("https://api.magicthegathering.io/v1/sets")
    

    # display the methods available to our new object 
    print( dir(resp) ) 



if __name__ == "__main__": 
    main()







