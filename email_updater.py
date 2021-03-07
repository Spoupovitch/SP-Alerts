import smtplib # Simple Mail Transfer Protocol client session object
import env # file for environment variables
from email.message import EmailMessage # allows setting of email message fields
import datetime as dt # differentiate email messages by timestamp
import os # check that output file exists

# Send an email with the JSON list of increasing tickers attached

ATTACHMENT = env.OUTPUT_FILE_NAME
ATTACHMENT_PATH = env.OUTPUT_FILE_PATH
TIMESTAMP = str(dt.datetime.now().time().strftime("%H:%M:%S"))

# construct email
msg = EmailMessage()
msg['From'] = env.EMAIL_SENDER
msg['To'] = env.EMAIL_RECEIVER
msg['Subject'] = 'Stock Data Update - ' + TIMESTAMP

if os.path.exists(ATTACHMENT_PATH):
    # attach increasing tickers list
    with open(ATTACHMENT_PATH, 'r') as inc_tickers:
        f_data = inc_tickers.read()
        inc_tickers.close()

    msg.add_attachment(f_data, subtype='json', filename=TIMESTAMP + '_' + ATTACHMENT)
    # --DEBUG--
    #print(msg)
else:
    # TODO - this logic needs to be accompanied by an automatic delete function
    msg.set_content('No data to update.')

# use SMTP class w SSL connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(env.EMAIL_SENDER, env.EMAIL_PASSWORD)
    smtp.send_message(msg)