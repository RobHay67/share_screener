import os

from results.view import results
from ticker.helpers.read_csv import load_a_ticker


def verify_file_exists_before_loading(scope, ticker):
	if os.path.exists( scope.path_share_data_file ):
		load_a_ticker(scope, ticker )
		scope.downloaded_loaded_list.append(ticker)
		results( scope, ticker, result='passed' )
	else:
		scope.downloaded_missing_list.append(ticker)
		results( scope, ticker, result='failed' )