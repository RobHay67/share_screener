
from config.results.store import store_result
from data.tickers.model.ticker_path import path_for_ticker_file


def save_tickers(scope):
	page 		= scope.pages['display_page']
	ticker_list = scope.pages[page]['ticker_list']
	
	store_result( 	scope, 
				passed='Saved > ', 
				failed='Save Cancelled (no data) > ', 
				passed_2='na'
				)

	for ticker in ticker_list:
		if ticker in scope.data['ticker_files']:						# if its not in here, it will not be available to save
			path_for_ticker_file(scope, ticker )
			save_ticker( scope, scope.data['ticker_files'][ticker] )
			store_result( scope, ticker, result='passed' )
		else:
			store_result( scope, ticker, result='failed' )
	
	store_result(scope, 'Finished', final_print=True )



def save_ticker( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.files['paths']['ticker_data'], index=False )



