from alpha_vantage.timeseries import TimeSeries # stock data retrieval API

return TimeSeries(key=env.ALPHA_VANTAGE_API_KEY, output_format='json')