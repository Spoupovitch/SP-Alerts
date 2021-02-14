# data analysis library
import pandas as pd
# stock data retrieval API
from alpha_vantage.timeseries import TimeSeries
# set starting and ending dates
import datetime as dt
import time
import json
# file for environment variables
import env
# needed for file operations
import os

# Take in a JSON list of stock ticker symbols
# Calculate percentage increase for each symbol
# Compile a JSON list of any increases above the threshold

if os.path.exists(env.CACHE_PATH):
    # delete python cache folder
    os.remove(env.CACHE_PATH)

    # delete cache's parent folder
    #os.rmdir(env.CACHE_DIR)
else:
    print("Cache does not exist, none deleted")

# read in a list of company tickers as data frame to check
ticker_list = pd.read_json('company_list.json')
#print("Tickers to check:", ticker_list)

# list of tickers and changes to send in email
alert_list = {}

# loop thru ticker list
for symbol in ticker_list['Symbol']:
    # DEBUG
    #print()
    #print("Checking symbol:", symbol)

    # create time series
    ts = TimeSeries(key=env.ALPHA_VANTAGE_API_KEY, output_format='json')
    data = ts.get_quote_endpoint(symbol)
    #print(data)

    pct_chg = data[0].get('10. change percent')
    # remove '%' and round percentage change
    print(symbol, "price change %:", round(float(pct_chg[:-1]), 2))

    if abs(pct_chg > env.PCT_CHG_THRESHOLD):
        # DEBUG
        #print(symbol, "price increased above threshold")

        # add symbol and price increase % to alert list
        alert_list.__setitem__(symbol, pct_chg)


# write results to output file
with open('crap.json', 'w') as output_file:
    print(json.dumps(alert_list, indent=2), file=output_file)