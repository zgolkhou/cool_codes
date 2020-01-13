# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:12:24 2013

@author: Zach

please modify the message as you wish.
"""

import smtplib

SUBJECT = "Test email from Python"
fromaddr = 'emial_address'  
toaddrs  = 'phone_number@vtext.com'  
#msg = 'Hi! The processing is done!'  
msg = 'The code is still running!'
  
# Credentials (if needed)  
username = 'username'  
password = 'password'  

# The actual mail send  
server = smtplib.SMTP('smtp.gmail.com:587')  
server.starttls()  
server.login(username,password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()  

"""
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
"""
