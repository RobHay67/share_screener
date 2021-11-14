import os
import pathlib

# Folders
def scope_folders(scope):
	scope.folder_project = pathlib.Path(__file__).parent.parent.resolve()
	scope.folder_share_data = pathlib.Path.home().joinpath( scope.folder_project, 'files' )
	scope.folder_results_analysis = pathlib.Path.home().joinpath( scope.folder_project, scope.folder_share_data, 'results_analysis' )
	scope.folder_website = pathlib.Path.home().joinpath( scope.folder_project, scope.folder_share_data, 'website' )
	if not os.path.isdir( scope.folder_project ) : os.makedirs( scope.folder_project )
	if not os.path.isdir( scope.folder_share_data ) : os.makedirs( scope.folder_share_data )
	if not os.path.isdir( scope.folder_results_analysis ) : os.makedirs( scope.folder_results_analysis )
	if not os.path.isdir( scope.folder_website ) : os.makedirs( scope.folder_website )
	# File Paths
	scope.path_ticker_index = pathlib.Path.home().joinpath( scope.folder_share_data, 'ticker_index.csv' )
	scope.path_website_file = pathlib.Path.home().joinpath( scope.folder_website, 'strategy_results.json' )
	scope.path_share_data_file = 'not yet set',