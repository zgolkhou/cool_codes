# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:12:24 2013

@author: Zach
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

