#!/usr/bin/env python3 

# make the smtplib module available
import smtplib
# secret acceptance of password 
import getpass 


def main(): 
    myaddress = input("Enter your mail.com address: ")
    mypass = getpass.getpass("Enter your Password: ")

    content = f"""From:{myaddress}\n
    Subject:Testing a subject line 1 time!\nPSI limit at maximum, built more pylons."""
    # enter server info
    mail = smtp.SMTP('smtp.mail.com',587)
    # for handshaking 
    mail.ehlo()
    # start an encrypted connection 
    mail.starttls()
    # log into your account 
    mail.login(myaddress, mypass)


    # send from, send to, what to send 
    mail.sendmail(myaddress, 'wilmerdanny@icloud.com', content)
    # end the connection
    mail.close()


# call the main function 
main()



