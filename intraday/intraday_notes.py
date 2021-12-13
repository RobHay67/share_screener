# Test Daily Info and charting

# load up the daily share data for a particular share
# plot it
# try and predict price movemment by volume

import pandas as pd

import yfinance as yf
pd.options.display.max_rows = 999
# import hvplot.pandas
# import matplotlib.pyplot as plt


## Establish Ticker and any other vriables
ticker = 'lic.ax'

period   = '2d'
interval = '5m'




## load the daily data for the specified ticker


yf_download = yf.download( ticker, period=period, interval=interval, progress=True, show_errors=False )

yf_download = yf_download.sort_index(ascending=False)        # ensure latest trade is at the top of the list

print ( 'Total Daily Volume =', yf_download.Volume.sum())
# TODO  make this into a report

# ensure the index is a datetime object
# yf_download.index = pd.to_datetime(yf_download.index, format='%Y-%m-%d %H:%M:%S')
yf_download.index = yf_download.index.tz_localize(None)


yf_download.head(5)






## Add a Cumulative Sum to our Share code



# add a date only column for the cumulative sum
yf_download['date_only'] = pd.to_datetime(yf_download.index).date

# ensure the new date_only field is stored as a date
yf_download['date_only'] = pd.to_datetime(yf_download['date_only'])

print ( yf_download.date_only.value_counts() )
yf_download.sample(3)


# short cut for testing
yf_download = yf_download.sample(20)
yf_download.date_only.value_counts()


# sort by the index so that the trades are in the correct order (ascending)
yf_download = yf_download.sort_index(ascending=True)

yf_download.head(2)


# add a cumulative total - but for each day

yf_download["cum_sum"] = yf_download["Volume"].groupby(yf_download['date_only']).cumsum()
yf_download


yf_download.dtypes

# take a copy of the df as we need to modify it for plotting
plot_data = yf_download.copy()
plot_data = plot_data.reset_index()
plot_data


plot_data.plot(x='date_only', y="cum_sum", kind="line")


