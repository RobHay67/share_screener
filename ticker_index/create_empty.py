
import pandas as pd
from ticker_index.save import save_index



def create_empty_ticker_index(scope):

	scope.ticker_index['render']['missing_ticker_index_file'] = True
	scope.ticker_index['render']['created_empty_ticker_index_file'] = True

	dataframe_columns = []
	for column_name in scope.ticker_index['schema']: 
		dataframe_columns.append(column_name)
		ticker_index = pd.DataFrame(columns=dataframe_columns)

	ticker_index.set_index('share_code', inplace=True)
	
	# remove any delisted stocks here
	
	scope.ticker_index['df'] = ticker_index
	
	save_index(scope)