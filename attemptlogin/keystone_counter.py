#!/usr/bin/env python3 


# succesful --->   -] Authorization failed
# failed ---->  - - - - -] Authorization failed






# keystone.common.wsgi
loginfail = 0 

# open the file for reading 
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")
# turn the file into a list of lines in memory
keystone_file_lines=keystone_file.readlines()
# loop over the list of lines 
for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed log in attempts is", loginfail)
keystone_file.close()


