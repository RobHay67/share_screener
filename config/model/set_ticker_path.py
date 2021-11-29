import pathlib


# -----------------------------------------------------------------------------------------------------------------------------------
# share file path generator
# -----------------------------------------------------------------------------------------------------------------------------------

def path_for_ticker_file( scope, ticker ):
	file_name = ( ticker.replace( '.', '_' ) ) + '.csv'
	file_path = pathlib.Path.home().joinpath( scope.folder_share_data, file_name )
	scope.path_ticker_data_file = file_path


