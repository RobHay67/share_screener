import logging
import pandas as pd
import os

from files.helpers.ticker_path import path_for_ticker_file
from tickers.model.new import add_new_ticker_data
from tickers.model.missing.failed_load import fail_local_load_event


def load_ticker(scope, ticker):
	logging.warning(f"load_ticker {ticker=}")
	path_for_ticker_file(scope, ticker, 'load')
	# Check that a local file is available to load
	if os.path.exists( scope.files['paths']['ticker_data'] ):
		ticker_data_file = pd.read_csv (  
									scope.files['paths']['ticker_data'], 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = scope.ticker_schema['usecols'],
									# index_col   = 'date', 
									dtype       = scope.ticker_schema['dtypes'],
									parse_dates = scope.ticker_schema['dates'],
									)
		add_new_ticker_data(scope, ticker, ticker_data_file)
		
	else:
		# The expected Local file is not available
		fail_local_load_event(scope, ticker)		

	# the ticker either loaded, or failed to load. 
	# either way we need to remove it from the list to load
	page = scope.display['page']
	scope.page[page]['list_load_tickers'].remove(ticker)



	







