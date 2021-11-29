import os
import pathlib
import pandas as pd

from config.model.set_results import store_results


from config.model.set_ticker_path import path_for_ticker_file


def save_tickers(scope):
	page 		= scope.page_to_display
	ticker_list = scope.pages[page]['ticker_list']

	store_results( 	scope, 
				passed='Saved > ', 
				failed='na', 
				passed_2='na'
				)

	for ticker in ticker_list:
		path_for_ticker_file(scope, ticker )
		save_ticker( scope, scope.ticker_data_files[ticker] )
		store_results( scope, ticker, result='passed' )
	
	store_results(scope, 'Finished', final_print=True )



def save_ticker( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.path_ticker_data_file, index=False )



