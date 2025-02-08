import logging
import os
import pandas as pd
from ticker_index.helpers.create_empty import create_empty_ticker_index


def load_ticker_index_file( scope ):
	logging.warning("load_ticker_index_file")
	if os.path.exists( scope.files['paths']['ticker_index'] ):
		
		ticker_index_file = pd.read_csv(  scope.files['paths']['ticker_index'], 
									dtype=scope.ticker_index['lists']['csv_dtypes'],
									parse_dates=scope.ticker_index['lists']['csv_dates'],
									)

		ticker_index_file.set_index('share_code', inplace=True)
		
		# remove any delisted stocks here

		if len(ticker_index_file) > 0:
			ticker_index_file['listing_date'] = pd.to_datetime( ticker_index_file['listing_date'].dt.date  )

		scope.ticker_index['df'] = ticker_index_file	# Cache the loaded ticker Index file	

	else: 
		create_empty_ticker_index(scope)
		

	






