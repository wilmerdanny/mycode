#!/usr/bin/env python3 

# open file in read mode 
with open("dnsservers.txt", "r") as dnsfile: 
    # loop across the lines in the file 
    for i in dnsfile: 
        print(i, end="")




