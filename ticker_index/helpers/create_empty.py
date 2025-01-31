import logging
import pandas as pd

from ticker_index.scope.model.save import save_index
from ticker_index.scope.views.dataframes.messages import message_missing_ticker_file
from ticker_index.scope.views.dataframes.messages import messgae_creation_success


def create_empty_ticker_index(scope):
	logging.debug("create_empty_ticker_index")
	message_missing_ticker_file(scope)

	dataframe_columns = []
	for column_name in scope.ticker_index['schema']: 
		dataframe_columns.append(column_name)
		ticker_index = pd.DataFrame(columns=dataframe_columns)

	ticker_index.set_index('share_code', inplace=True)
	
	# remove any delisted stocks here
	
	scope.ticker_index['df'] = ticker_index
	
	messgae_creation_success()

	save_index(scope)
