import smtplib # Simple Mail Transfer Protocol client session object
import env # file for environment variables
from email.message import EmailMessage # allows setting of email message fields
import datetime as dt # differentiate email messages by timestamp

# Send an email alerting user to archive the day's updates

TIMESTAMP = str(dt.datetime.now().time().strftime("%H:%M:%S"))

# construct email
msg = EmailMessage()
msg['From'] = env.EMAIL_SENDER
msg['To'] = env.EMAIL_RECEIVER
msg['Subject'] = 'Apply Email Filter - ' + TIMESTAMP
msg.set_content('CLEAN UP STOCK PRICE UPDATES')

# DEBUG
#print(msg)

# use SMTP class w SSL connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(env.EMAIL_SENDER, env.EMAIL_PASSWORD)
    smtp.send_message(msg)