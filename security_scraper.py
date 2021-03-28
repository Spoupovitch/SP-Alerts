import sys # work with command line arguments
import env # file for environment variables


# Retrieve a list of all securities to be monitored throughout the day.

ts = sys.argv[1]
data = ts.get_symbol_search("A")

print(data)