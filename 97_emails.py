#Checkout
#https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/

import smtplib
conn = smtplib.SMTP('smtp.gmail.com',587) # different for different email providers 465

conn.ehlo() # weird history , can be ommited
conn.starttls() # for encrypted password sending

#conn.ehlo() # can be ommited
conn.login('123@gmail.com', '@#$#@%@#$%#$%') # email, password

emailBody = '''subject: so long ...\n\n
Dear Ian 
hope you have a good time i college.
With love Macros
''' # after the new-lines comes the main body

emailBody2 = '''Testing Python email ...\n\n
This\n
is awesome\n\n
sutff
'''

#send mail supports sending multiple email.
conn.sendmail('123@gmail.com', ['456@gmail.com'], emailBody2) #args: first is for FROM , second in for TO

#when sendmail is done it ruturns a dictionary with the failed attemps. 
#If everything is fine the you will get {} 
print(emailBody2)
conn.quit() # diconnect from smtp server

#https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/
#https://www.raspberrypi.org/forums/viewtopic.php?t=86762




#Checking your email
# pip install imapclient
# pip install pyzmail
import pyzmail
import imapclient
conn =  imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('123@gmail.com','@#$#@%@#$%#$%')

conn.select_folder('INBOX', readonly=True)

#Imap seach keys
UIDs = conn.search(['SINCE 20-Aug-2015']) # need to pass it as a list of strings for imap. Returns unique ids for the emails, you need specific formatting for the date

rawMessage = conn.fetch([41454], ['BODY', 'FLAGS']) # to que the raw email
message = pyzmail.Pyzmail.factory(rawMessage[41454][b'BODY[]']) # this is required to exatract the information correctly. search for IMAP cheat sheet

message.get_subject() # pyzmail gives you util fucntions to exatract what you need
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

message.text_part #this shows if the email has text in it 
message.html_part #this shows if the email has html in it 

#to get the actual email text
message.text_part.get_payload().decode('UTF-8') #99% it will be UTF
message.text_part.charset == None # to check text format

#to search for folders in you email account 
conn.list_folders()

conn.select_folder('INBOX', readonly=False)# to modify folders you can do:
UIDs = conn.search(['SINCE 20-Aug-2015'])

conn.delete(UIDs)

conn.logout()


#https://imapclient.readthedocs.org
#http://wwww.magiksys.net/pyzmail
#https://automatetheborignstuff.com/chapter16







