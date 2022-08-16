import pandas as pd

from progress.cache import cache_progress
from tickers.schema import ticker_file_usecols
from tickers.status.combine import set_data_status
from tickers.cache import cache_ticker_file

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Combiner
#   	concatenates any downloaded data with any loaded data 
# 		resulting in a complete (hopefully) temporal history of existing share data
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def combine_loaded_and_downloaded_ticker_data(scope):

	cache_progress(scope, 
			passed='Combined > ', 
			passed_2='Created NEW Local files > ', 
			failed='na' 
			)

	app = scope.apps['display_app']

	ticker_list = scope.apps[app]['selected_tickers']

	# iterate through the target tickers for the App
	for ticker in ticker_list:
		
		downloaded_ticker_list = scope.download['yf_files']['ticker'].unique()
		
		# Check if we have downloaded data (we may have nothing)
		if ticker in downloaded_ticker_list:
			

			# subset to a specific ticker from the downloaded data
			ticker_data = scope.download['yf_files'][scope.download['yf_files']['ticker'] == ticker]			
			ticker_data = ticker_data[ticker_file_usecols]				# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]		# drop rows where volume is zero 


			# We may have no data after dropping the zero volume rows
			if len(ticker_data)>0:
				
				if ticker in scope.tickers.keys():	
					# we have an exisiting share_data_file so we concatenate the data
					scope.tickers[ticker]['df'] = pd.concat([scope.tickers[ticker]['df'], ticker_data]).drop_duplicates(subset=['date'], keep='last')
					# sort the share data into date order ascending
					scope.tickers[ticker]['df'].sort_values(by=['date'], inplace=True, ascending=False)		
					cache_progress( scope, ticker, result='passed' )
				else:
					# its brand new - so we can just add it to the dictionary
					cache_ticker_file(scope, ticker, ticker_data)
					cache_progress( scope, ticker, result='passed_2' )
				
				
				set_data_status(scope, ticker)
		
		
		
	cache_progress(scope, 'Finished', final_print=True )


