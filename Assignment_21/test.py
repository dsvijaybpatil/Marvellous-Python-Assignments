import smtplib 
from email.message import EmailMessage
import ssl

email_sender="patilvijay.95@gmail.com"
email_password="mhpb awkv bjpj ngba"
email_receiver="marvellousinfosystems@gmail.com"

subject="This is testing mail."
body="Sending mail"


em=EmailMessage()
em['from']=email_sender
em['to']=email_receiver
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',365,context=context) as smtp:
    smtp.login(email_sender,email_receiver)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

print("Mail sent successfully.")
