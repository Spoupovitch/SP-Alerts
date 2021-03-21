import schedule # execute commands at set interval
import datetime as dt # constrict execution window
from pytz import timezone # market time is EST
import time # manipulate time values - minutes (0-59)
import os # use to call other scripts
import sys # allow scheduler to end execution

# Call python scripts at a set interval
# MAIN SWITCH for running update scripts

OPEN_TIME = dt.datetime.strptime("09:30", "%H:%M").strftime("%H:%M")
CLOSE_TIME = dt.datetime.strptime("16:00", "%H:%M").strftime("%H:%M")

SCRAPE_SCRIPT = 'stock_data_scraper.py'
MAIL_SCRIPT = 'email_updater.py'
EOD_ALERT = 'eod_email.py'

def scrape_stock_data():
    os.system(SCRAPE_SCRIPT)

def send_email():
    os.system(MAIL_SCRIPT)

# set interval for executing scripts
schedule.every(1).minute.do(scrape_stock_data)
schedule.every(1).minute.do(send_email)

while 1:
    CURR_TIME = dt.datetime.now(timezone('EST')).strftime("%H:%M")

    # logic for discerning when markets are closed
    if CURR_TIME < OPEN_TIME or CLOSE_TIME < CURR_TIME or dt.datetime.today().weekday() > 4:
        # send email reminder to apply filter
        os.system(EOD_ALERT)
        sys.exit("Markets are closed, exiting.")

    schedule.run_pending()
    # delay execution for given # of seconds
    time.sleep(1)