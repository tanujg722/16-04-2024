import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
#print(smtp_object.ehlo())
#print(smtp_object.starttls())
#tpassword = input('What is your password: ')

import getpass
#password = getpass.getpass('Password please:') # secured way to pass the imfo

email = getpass.getpass("Email: ")
password = getpass.getpass('Password: ')
smtp_object.login(email,password)