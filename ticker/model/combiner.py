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
		if ticker in scope.download_yf_files['ticker'].unique():										# if we have downloaded data (we may have nothing)
			ticker_data = scope.download_yf_files[scope.download_yf_files['ticker'] == ticker]			# subset to a specific ticker in the downloaded data
			ticker_data = ticker_data[ticker_file_usecols]												# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]										# drop rows where volume is zero 
			if ticker in scope.downloaded_loaded_list:													# we have an exisiting share_data_file so we concatenate the data
				scope.ticker_data_files[ticker] = pd.concat([scope.ticker_data_files[ticker], ticker_data]).drop_duplicates(subset=['date'], keep='last')
				store_results( scope, ticker, result='passed' )
				

			else:
				scope.ticker_data_files[ticker] = ticker_data											# its brand new - so we can just add it to the dictionary
				store_results( scope, ticker, result='passed_2' )
			scope.ticker_data_files[ticker].sort_values(by=['date'], inplace=True, ascending=False)		# sort the share data into date order ascending

			set_refresh_df_for_ticker_in_all_pages(scope, ticker, True)
					
	store_results(scope, 'Finished', final_print=True )


