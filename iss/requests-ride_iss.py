#!/usr/bin/python3


# notice we no longer need to import urllib.request or json 
import requests 


# define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'


def main():
    """runtime code"""


    # call the webservice 
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()



    # translate the json into python lists and dictionaries 
    helmetson = groundctrl.json()


    # display our pythonic data 
    print("\n\nConverted Python Data")
    print(helmetson) 

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people) 


if __name__ == '__main__': 
    main()



