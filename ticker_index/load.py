import os
import pandas as pd

from partials.dropdowns.dropdowns import refresh_dropdown_lists

from ticker_index.schema import schema
from ticker_index.schema import csv_dates
from ticker_index.schema import csv_dtypes
from ticker_index.save import save_index


from ticker_index.view.messages import message_title
from ticker_index.view.messages import message_loading
from ticker_index.view.messages import message_loaded
from ticker_index.view.messages import message_missing_index_file
from ticker_index.view.messages import message_new_index_file


def load_ticker_index_file( scope ):
	# message_title()

	if os.path.exists( scope.files['paths']['ticker_index'] ):
		# message_loading(scope)
		
		ticker_index = pd.read_csv(  scope.files['paths']['ticker_index'], 
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)

		ticker_index['listing_date'] = pd.to_datetime( ticker_index['listing_date'].dt.date  )
		ticker_index.set_index('share_code', inplace=True)
		
		# remove any delisted stocks here

		scope.ticker_index = ticker_index		

		refresh_dropdown_lists(scope)

	else: 
		message_missing_index_file(scope)

		dataframe_columns = []
		for column_name in schema: 
			dataframe_columns.append(column_name)
			ticker_index = pd.DataFrame(columns=dataframe_columns)

		message_new_index_file()

		ticker_index.set_index('share_code', inplace=True)
		
		# remove any delisted stocks here
		
		scope.ticker_index = ticker_index
		
		save_index(scope)






