import pandas as pd
import os

from files.path import path_for_ticker_file
from tickers.cache import cache_ticker_data
from tickers.events.missing_local_file import missing_file_event
from tickers.events.add_ticker import add_ticker_event

from tickers.schema import ticker_file_usecols
from tickers.schema import ticker_file_dtypes
from tickers.schema import ticker_file_dates



def load_ticker(scope, ticker):
	path_for_ticker_file(scope, ticker )
	# Check that a local file is available to load
	if os.path.exists( scope.files['paths']['ticker_data'] ):
		ticker_data_file = pd.read_csv (  
									scope.files['paths']['ticker_data'], 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = ticker_file_usecols,
									# index_col   = 'date', 
									dtype       = ticker_file_dtypes,
									parse_dates = ticker_file_dates,
									)
		add_ticker_event(scope, ticker)
		cache_ticker_data(scope, ticker, ticker_data_file)
	else:
		# The expected Local file is not available
		missing_file_event(scope, ticker)		



	







