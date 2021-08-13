#!/usr/bin/env python3


#  So you can enter things like, *.txt or *.pcap, but 
# will NOT try looking in directories described in the global EXCLUDE list.


import os 
import fnmatch 

exclude = ["/usr", "/home", "/var"]



def find(pattern, path): 
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE:
            dirs[:] = []
            files[:] = []
        for name in files:
            if fnmatch.fnmatch(name, patter): 
                result.append(os.path.join(root, name))
    return result 



def main():
    """runtime code"""
    lookfor = (input("What pattern am I looking for (Example: *.txt or *.cfg) "))
    lowerLookfor = lookfor.lower()
    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(lowerLookfor, lookwhere)) # call function

main()


 
