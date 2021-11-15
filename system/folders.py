import os
import pathlib
import streamlit as st

from system.reports import view_3_columns

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
	scope.path_share_data_file = 'not yet set'




def view_folders(scope):
	

	diff_col_size = [2,6,2]
	st.subheader('Folders')
	view_3_columns( 'Project', scope.folder_project, 'folder_project', diff_col_size )
	view_3_columns( 'Share Data', scope.folder_share_data, 'folder_share_data', diff_col_size )
	view_3_columns( 'Results Analysis', scope.folder_results_analysis, 'folder_results_analysis', diff_col_size )
	view_3_columns( 'Website Output', scope.folder_website, 'folder_website', diff_col_size )

	st.subheader('Paths to Specific Objects')
	view_3_columns( 'Path for Share Index File', scope.path_ticker_index, 'path_ticker_index', diff_col_size )
	view_3_columns( 'Path for Website Output File', scope.path_website_file, 'path_website_file', diff_col_size )
	view_3_columns( 'Path for Share Data File', scope.path_share_data_file, 'path_share_data_file', diff_col_size )
