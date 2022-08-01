import os
import pandas as pd

from apps_parts.dropdowns import refresh_dropdown_lists

from data.index.schema import schema
from data.index.schema import csv_dates
from data.index.schema import csv_dtypes
from data.index.save import save_index


from data.index.view.messages import message_title
from data.index.view.messages import message_loading
from data.index.view.messages import message_loaded
from data.index.view.messages import message_missing_index_file
from data.index.view.messages import message_new_index_file


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

		scope.data['ticker_index'] = ticker_index		

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
		
		scope.data['ticker_index'] = ticker_index
		
		save_index(scope)






