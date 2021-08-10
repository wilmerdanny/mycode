#!/usr/bin/env python3


#ask user to offer bid on PS5
bid = float(input("Please enter your bid for this PS5:"))


if bid > 499:
    print("You said", bid, "Wow, entering scammer territory")
elif bid == 499:
    print("You said" , bid , "This is the correct bid amount.")
else:
    print("Sorry," , bid , "is just too low")




