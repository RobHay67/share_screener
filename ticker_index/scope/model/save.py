import logging
from ticker_index.scope.views.dataframes.messages import message_saved_ticker_index_file


def save_ticker_index(scope):
	logging.warning("save_ticker_index")
	saving_df = scope.ticker_index['df'].copy()
	# ensure that the index is saved as a normal column
	saving_df.reset_index(inplace=True)      	 
	saving_df.to_csv( scope.files['paths']['ticker_index'], index=False )

	message_saved_ticker_index_file()
	print ( '\033[92m' + 'Saving the Ticker Index file Now ' + '>'*50 + '\033[0m')	



 
def save_changes_into_ticker_index(scope, edited_df):
	logging.warning("save_changes_into_ticker_index")
	scope.ticker_index['df'] = edited_df
	save_ticker_index(scope)
	scope.ticker_index['save_edited_df'] = False





