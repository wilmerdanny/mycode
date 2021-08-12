#!/usr/bin/env python3


# script to search and find all matches 
import os 

# define a function that can
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files: 
            result.append(os.path.join(root, name))
    return result 


lookfor = input("What am I looking for? ") 
lookwhere = input("What is the path in which I should search? ")

print(find_all(lookfor, lookwhere))


