#!/usr/bin/env python3 


import requests 

# define NEOW URL

NEOWURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials 
def returncreds():
    with open("/home/student/nasa.creds","r") as mycreds: 
        nasacreds = mycreds.read()
    # remove any new line characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds 


# this is our main function 
def main():
    # first grab credentials 
    nasacreds = returncreds()


    # update the date below, if you'd like 
    startdate = "start_date=2021-08-16"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOWURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
    
