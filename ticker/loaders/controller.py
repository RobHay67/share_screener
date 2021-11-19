import os

from results.view import results
from ticker.helpers.path import generate_path_for_share_data_file
from ticker.loaders.load import load_a_ticker



def load_ticker_or_tickers(scope, ticker=None):
	results(scope, 
			passed='LOADED Share Data Files > ', 
			failed='MISSING Share Data Files for > ', 
			passed_2='na',
			)

	if ticker != None:
		ticker_list = [ticker]
	else:
		ticker_list = scope.selected['multi']['ticker_list']
	
	for ticker in ticker_list:
		generate_path_for_share_data_file(scope, ticker )
		verify_existence_and_load(scope, ticker)

	results(scope, 'Finished', final_print=True )


def verify_existence_and_load(scope, ticker):
	if os.path.exists( scope.path_share_data_file ):
		load_a_ticker(scope, ticker )
		scope.downloaded_loaded_list.append(ticker)
		results( scope, ticker, result='passed' )
	else:
		scope.downloaded_missing_list.append(ticker)
		results( scope, ticker, result='failed' )







