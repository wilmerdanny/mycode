#!/usr/bin/env python3

# this script will do the same thing as the other file, but uses "with"
# open file in read mode 
with open("dnsservers.txt", "r") as dnsfile: 
    dnslist = dnsfile.readlines()
    for svr in dnslist:
        print(svr, end="")

# no need to add close statement, with executes that automatically. 



