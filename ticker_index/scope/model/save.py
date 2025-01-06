from ticker_index.scope.views.dataframes.messages import message_saved_ticker_index_file


def save_index(scope):
	
	saving_df = scope.ticker_index['df'].copy()
	
	# ensure that the index is saved as a normal column
	saving_df.reset_index(inplace=True)      	 
	
	saving_df.to_csv( scope.files['paths']['ticker_index'], index=False )

	message_saved_ticker_index_file()
	print ( '\033[92m' + 'Saving the Ticker Index file Now ' + '>'*50 + '\033[0m')	



 
def save_changes_into_ticker_index(scope, edited_df):

	scope.ticker_index['df'] = edited_df
	save_index(scope)
	scope.ticker_index['render']['save_edited_df'] = False





