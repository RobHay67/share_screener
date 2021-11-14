import os
import pathlib
import pandas as pd

from system.render import results


from ticker.path import generate_path_for_share_data_file



def save_tickers( scope ): # DONE
	results( scope, passed='Files SAVED > ', failed='na', passed_2='na' )
	for ticker in scope.share_data_files:
		generate_path_for_share_data_file(scope, ticker )
		save_ticker( scope, scope.share_data_files[ticker] )
		results( scope, ticker, result='passed' )
	results(scope, 'Finished', final_print=True )

def save_ticker( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.path_share_data_file, index=False )



