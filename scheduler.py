import schedule # execute commands at set interval
import time # manipulate time values - minutes (0-59)
import os # use to call other scripts

# Call python scripts at a set interval

SCRAPER_SCRIPT = "stock_data_scraper.py"
MAIL_SCRIPT = "mail_handler.py"

def crap():
    os.system(SCRAPER_SCRIPT)

def crapola():
    os.system(MAIL_SCRIPT)

# set interval for executing scripts
schedule.every(1).minute.do(crap)
schedule.every(1).minute.do(crapola)

while 1:
    schedule.run_pending()
    # delay execution for given # of seconds
    time.sleep(1)