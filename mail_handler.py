import smtplib
import env
from email.message import EmailMessage
import datetime as dt

# construct email
msg = EmailMessage()
msg['From'] = env.EMAIL_SENDER
msg['To'] = env.EMAIL_RECEIVER
msg['Subject'] = 'Stock data' + str(dt.datetime.now())
msg.set_content('GFY')

# use simple mail transfer protocol class w SSL connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(env.EMAIL_SENDER, env.EMAIL_PASSWORD)

    smtp.send_message(msg)