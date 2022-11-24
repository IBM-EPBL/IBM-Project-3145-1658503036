import smtplib
import sendgrid as sg
import os
SUBJECT = "Expense Tracker"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("akashkumar992002@gmail.com", "******")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("akashkumar992002@gmail.com", email, message)
    s.quit()
