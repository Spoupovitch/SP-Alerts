import pandas as pd # data analysis library
import json
import sys # work with command line arguments
import env # file for environment variables
import os # needed for file operations

# Take in a JSON list of stock symbols
# Calculate percentage increase for each symbol
# Compile a JSON list of any increases above the threshold

PCT_CHG_THRESHOLD = 1
SECURITY_LIST = './assets/json/company_list.json'

# read in a list of stocks as data frame to check
security_list = pd.read_json(SECURITY_LIST)

# list of securities and price change percents to send in email
alert_list = {}

# delete python cache
if os.path.exists(env.CACHE_PATH):
    os.remove(env.CACHE_PATH)
else:
    print("No cache found at", env.CACHE_PATH)

# loop thru security list
for symbol in security_list['Symbol']:
    # create time series
    ts = sys.argv[1]
    data = ts.get_quote_endpoint(symbol)

    # algo to calculate price percentage change since BOD
    #pct_chg = round((curr_prc - open_prc) / open_prc * 100, 2)
    
    pct_chg = data[0].get('10. change percent')
    # remove '%', parse float and round percentage change
    pct_chg = round(float(pct_chg[:-1]), 2)

    # --DEBUG--
    print('\n', "Checking symbol:", symbol)
    print(symbol, "price change %:", pct_chg)

    if abs(pct_chg) > PCT_CHG_THRESHOLD:
        # save symbol and price change %
        alert_list.__setitem__(symbol, pct_chg)
        # --DEBUG--
        print(symbol, "increased above threshold")

# write results to output file
with open(env.OUTPUT_FILE_PATH, 'w') as output_file:
    print(json.dumps(alert_list, indent=2), file=output_file)