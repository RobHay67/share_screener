import pandas as pd
import os

from files.path import path_for_ticker_file
from tickers.new import add_new_ticker
from tickers.missing_tickers.failed_load import fail_local_load_event

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
		add_new_ticker(scope, ticker, ticker_data_file)
	else:
		# The expected Local file is not available
		fail_local_load_event(scope, ticker)		



	







