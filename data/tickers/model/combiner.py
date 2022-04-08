import pandas as pd

from config.results.results import store_result

from data.tickers.config import ticker_file_usecols

from pages.model.set_page_df_status import set_refresh_page_df_ticker

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Combiner
#   	concatenates any downloaded data with any loaded data 
# 		resulting in a complete (hopefully) temporal history of existing share data
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def combine_loaded_and_download_ticker_data(scope):

	store_result(scope, 
			passed='Combined > ', 
			passed_2='Created NEW Local files > ', 
			failed='na' 
			)

	page = scope.pages['display_page']

	ticker_list = scope.pages[page]['ticker_list']

	for ticker in ticker_list:																			# iterate through the target tickers
		refresh_status_for_ticker = False
		downloaded_ticker_list = scope.data['download']['yf_files']['ticker'].unique()
		if ticker in downloaded_ticker_list:															# if we have downloaded data (we may have nothing)
			ticker_data = scope.data['download']['yf_files'][scope.data['download']['yf_files']['ticker'] == ticker]			# subset to a specific ticker in the downloaded data
			ticker_data = ticker_data[ticker_file_usecols]												# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]										# drop rows where volume is zero 

			if len(ticker_data)>0:																		# We may have no data after dropping the zero volume rows
				if ticker in scope.data['ticker_files'].keys():											# we have an exisiting share_data_file so we concatenate the data
					scope.data['ticker_files'][ticker] = pd.concat([scope.data['ticker_files'][ticker], ticker_data]).drop_duplicates(subset=['date'], keep='last')
					store_result( scope, ticker, result='passed' )
				else:
					scope.data['ticker_files'][ticker] = ticker_data											# its brand new - so we can just add it to the dictionary
					store_result( scope, ticker, result='passed_2' )
				scope.data['ticker_files'][ticker].sort_values(by=['date'], inplace=True, ascending=False)		# sort the share data into date order ascending
				refresh_status_for_ticker = True
		set_refresh_page_df_ticker(scope, ticker, refresh_status_for_ticker)
	store_result(scope, 'Finished', final_print=True )


