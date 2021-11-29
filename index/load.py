import os
import pandas as pd


from config.initial_scope.index_schema import schema
from config.initial_scope.index_schema import csv_dates
from config.initial_scope.index_schema import csv_dtypes
from index.model.save import save_index


from index.view.load_messages import message_title
from index.view.load_messages import message_loading
from index.view.load_messages import message_loaded
from index.view.load_messages import message_missing_index_file
from index.view.load_messages import message_new_index_file


def load_ticker_index_file( scope ):
	message_title()

	if os.path.exists( scope.path_ticker_index ):
		message_loading(scope)

		ticker_index = pd.read_csv(  scope.path_ticker_index, 
									dtype=csv_dtypes(schema),
									parse_dates=csv_dates(schema),
									)

		ticker_index['listing_date'] = pd.to_datetime( ticker_index['listing_date'].dt.date  )
		ticker_index.set_index('share_code', inplace=True)


		message_loaded()
		
		# remove any delisted stocks here

		scope.ticker_index = ticker_index
		scope.dropdown_lists_need_updating = True
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






