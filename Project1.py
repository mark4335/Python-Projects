from email.quoprimime import body_check
from multiprocessing import context
from email.massage import EmailMassage
from app2 import password
import ssl
import smtplib

email_sender ='personal_email'
email_password ='password'

email_receiver =''

subject ='Attention Needed'

body ="""
Your request and billing notice have been sent 
"""

em = EmailMassage()
em['From'] =email_sender
em['To'] =email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with  smtplib.SMTP_SSL('smtp.gamil.com',465, context=context) as smtp:
  	smtp.login(email_sender , email_password)
  	smtp.sendmail(email_sender ,email_receiver, em.as_string())
