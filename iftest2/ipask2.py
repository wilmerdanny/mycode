#!/usr/bin/env python3

ipchk = input("Apply an IP address: ")


# if user sets IP as Gateway
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not reccommended.")
elif ipchk: 
    print("Looks llike the IP address was set: " + ipchk)
else: 
    print("You did not provide input.")
