import pandas as pd

from config.model.set_results import store_results

from config.initial_scope.ticker import ticker_file_usecols

from config.model.set_page_df_refresh import set_refresh_df_for_ticker_in_all_pages


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Combiner
#   	concatenates any downloaded data with any loaded data 
# 		resulting in a complete (hopefully) temporal history of existing share data
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def combine_loaded_and_download_ticker_data(scope): # TODO - change to check for loaded ticker

	store_results(scope, 
			passed='Combined > ', 
			passed_2='Created NEW Local files > ', 
			failed='na' 
			)

	page = scope.page_to_display

	ticker_list = scope.pages[page]['ticker_list']

	for ticker in ticker_list:																			# iterate through the target tickers
		refresh_data_for_page = False
		downloaded_ticker_list = scope.download_yf_files['ticker'].unique()
		if ticker in downloaded_ticker_list:															# if we have downloaded data (we may have nothing)
			ticker_data = scope.download_yf_files[scope.download_yf_files['ticker'] == ticker]			# subset to a specific ticker in the downloaded data
			ticker_data = ticker_data[ticker_file_usecols]												# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]										# drop rows where volume is zero 

			if len(ticker_data)>0:																		# We may have no data after dropping the zero volume rows
				# if ticker in scope.loaded_ticker_list:													# we have an exisiting share_data_file so we concatenate the data
				if ticker in scope.ticker_data_files.keys():												# we have an exisiting share_data_file so we concatenate the data
					scope.ticker_data_files[ticker] = pd.concat([scope.ticker_data_files[ticker], ticker_data]).drop_duplicates(subset=['date'], keep='last')
					store_results( scope, ticker, result='passed' )
				else:
					scope.ticker_data_files[ticker] = ticker_data											# its brand new - so we can just add it to the dictionary
					store_results( scope, ticker, result='passed_2' )
				scope.ticker_data_files[ticker].sort_values(by=['date'], inplace=True, ascending=False)		# sort the share data into date order ascending
				refresh_data_for_page = True
			# 	set_refresh_df_for_ticker_in_all_pages(scope, ticker, True)
			# else:
			# 	set_refresh_df_for_ticker_in_all_pages(scope, ticker, False)
		set_refresh_df_for_ticker_in_all_pages(scope, ticker, refresh_data_for_page)
		# else:
		# 	set_refresh_df_for_ticker_in_all_pages(scope, ticker, False)			
	store_results(scope, 'Finished', final_print=True )


