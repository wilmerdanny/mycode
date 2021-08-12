#!/usr/bin/env python3 


# standard library imports go above 3rd party imports (best practice)
import re 
# python3 -m pip install requests 
import requests 


def main(): 
    print("Where should we search? ")
    url = input("> ")

    print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
    searchFor = input("> ")


    resp = requests.get(url)
    searchMe = resp.text 

    if re.search(searchFor, searchMe):
        print("Found a match!")
    else: 
        print("No match!")



if __name__ == "__main__":
    main()




