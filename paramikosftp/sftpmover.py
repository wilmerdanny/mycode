#!/usr/bin/env python3 

# moving files with SFTP 

# import paramiko so we can talk SSH 
import paramiko
import os 


# where to connect to 
t = paramiko.Transport("10.10.2.3", 22) ## IP and port


user_name = input(str("Please enter username: ")) 
user_password = input(str("Please enter password: "))


# how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username= user_name, password= user_password)


# make an sftp connetion object 
sftp = paramiko.SFTPClient.from_transport(t)


# iterate across files within the directory
for x in os.listdir("/home/student/filestocopy/"):
    if not os.path.isdir("/home/student/filestocopy/"+x): # find files, not dir
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target



# close the connection 
sftp.close()
