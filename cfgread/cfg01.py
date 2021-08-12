#!/usr/bin/env python3


##### EXPLORE READ #######

# create file object in 'r' read mode
configfile = open("vlanconfig.cfg", "r")

# display file to the screen - .read()
print(configfile.read())

# close file 
configfile.close()




###### EXPLORE READLINES ###########

# recreate file object to explore new method 
configfile = open("vlanconfig.cfg", "r")


# make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)


# iterate through configlist
for x in configlist:
    print(x)



# always close your file 
configfile.close()


