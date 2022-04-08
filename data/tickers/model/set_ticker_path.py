import pathlib


# -----------------------------------------------------------------------------------------------------------------------------------
# share file path generator
# -----------------------------------------------------------------------------------------------------------------------------------

def path_for_ticker_file( scope, ticker ):
	file_name = ( ticker.replace( '.', '_' ) ) + '.csv'
	file_path = pathlib.Path.home().joinpath( scope.files['folders']['tickers'], file_name )
	scope.files['paths']['ticker_data'] = file_path


