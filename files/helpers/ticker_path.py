import logging
import os




# generate path name based on the ticker code - on the fly


def path_for_ticker_file( scope, ticker ):
	logging.debug(f"path_for_ticker_file {ticker=}")
	file_name = ( ticker.replace( '.', '_' ) ) + '.csv'

	file_path = os.path.join(scope.files['folders']['tickers'], file_name)
	scope.files['paths']['ticker_data'] = file_path

