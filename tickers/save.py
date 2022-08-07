
from progress.store import cache_progress
from files.path import path_for_ticker_file

def save_tickers(scope):
	app 		= scope.apps['display_app']
	ticker_list = scope.apps[app]['ticker_list']
	
	cache_progress( scope, 
					passed='Saved > ', 
					failed='Save Cancelled (no data) > ', 
					passed_2='na'
					)

	for ticker in ticker_list:
		if ticker in scope.tickers:						# if its not in here, it will not be available to save
			path_for_ticker_file(scope, ticker )
			save_ticker( scope, scope.tickers[ticker]['df'] )
			cache_progress( scope, ticker, result='passed' )
		else:
			cache_progress( scope, ticker, result='failed' )
	
	cache_progress(scope, 'Finished', final_print=True )



def save_ticker( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.files['paths']['ticker_data'], index=False )



