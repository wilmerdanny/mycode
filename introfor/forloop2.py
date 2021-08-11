#!/usr/bin/env python3 


"""RZFeeser | Alta3 Research
   nesting an if-statement inside of a for loop"""

# create a list of strings 
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings 
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors 
for i in vendors:
    print("\nThe vendor is " + i, end="")
    if i not in approved_vendors: 
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")



