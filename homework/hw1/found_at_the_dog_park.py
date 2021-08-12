#!/usr/bin/env python3




#Write a script that will accept a list of items separated by a space from user input. 



# creating an empty list
list = []

# adding to list with user input
for i in range(5):
    item = input("List 5 items you're looking for at the dog park. ")
    list.append(item)




# Have your script then loop through that list and print each item 
# with the phrase "was found at the dog park" appended to it.

x = 0
while x <= len(list):
    print(f"{list[x]} was found at the dog park")
    x = x + 1




