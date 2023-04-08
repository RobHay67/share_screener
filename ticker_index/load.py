import os
import pandas as pd

from ticker_index.schema import csv_dates
from ticker_index.schema import csv_dtypes
from pages.header.selectors import refresh_dropdown_lists

from ticker_index.create_empty import create_empty_ticker_index


def load_ticker_index_file( scope ):

	if os.path.exists( scope.files['paths']['ticker_index'] ):
		
		ticker_index_file = pd.read_csv(  scope.files['paths']['ticker_index'], 
									dtype=csv_dtypes(scope),
									parse_dates=csv_dates(scope),
									)

		ticker_index_file.set_index('share_code', inplace=True)
		
		# remove any delisted stocks here

		if len(ticker_index_file) > 0:
			ticker_index_file['listing_date'] = pd.to_datetime( ticker_index_file['listing_date'].dt.date  )

		scope.ticker_index['df'] = ticker_index_file	# Cache the loaded ticker Index file	

		refresh_dropdown_lists(scope)

	else: 
		create_empty_ticker_index(scope)
		

	






