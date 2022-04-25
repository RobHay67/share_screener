import os

import streamlit as st
from pages.view.three_cols import three_cols



def scope_files(scope):

	scope.files = {}

	# Folders
	scope.files['folders'] = {}
	scope.files['folders']['project'] 			= os.path.abspath(os.curdir)
	scope.files['folders']['files'] 			= os.path.join(scope.files['folders']['project'], 'files')
	scope.files['folders']['tickers']			= os.path.join(scope.files['folders']['files']  , 'tickers')
	scope.files['folders']['results_analysis'] 	= os.path.join(scope.files['folders']['files'], 'results_analysis')
	scope.files['folders']['website'] 			= os.path.join(scope.files['folders']['files'], 'website')

	# Ensure that the folders exist
	if not os.path.isdir( scope.files['folders']['project'] ) 			: os.makedirs( scope.files['folders']['project'] )
	if not os.path.isdir( scope.files['folders']['tickers'] ) 			: os.makedirs( scope.files['folders']['tickers'] )
	if not os.path.isdir( scope.files['folders']['results_analysis'] ) 	: os.makedirs( scope.files['folders']['results_analysis'] )
	if not os.path.isdir( scope.files['folders']['website'] ) 			: os.makedirs( scope.files['folders']['website'] )
	
	# File Paths
	scope.files['paths'] = {}
	scope.files['paths']['ticker_index'] = os.path.join(scope.files['folders']['files'], 'ticker_index.csv')
	scope.files['paths']['ticker_data'] = 'not yet set'
	scope.files['paths']['website'] = os.path.join(scope.files['folders']['website'], 'strategy_results.json')




def view_folders(scope):

	diff_col_size = [2,6,2]

	st.subheader('Folders')
	three_cols( 'Project', scope.files['folders']['project'], 'folder_project', diff_col_size )
	three_cols( 'Files', scope.files['folders']['files'], 'folder_files', diff_col_size )
	three_cols( 'Share Data', scope.files['folders']['tickers'], 'folder_tickers', diff_col_size )
	three_cols( 'Results Analysis', scope.files['folders']['results_analysis'], 'folder_results_analysis', diff_col_size )
	three_cols( 'Website Output', scope.files['folders']['website'], 'folder_website', diff_col_size )

	st.subheader('Paths to Specific Objects')
	three_cols( 'Path for Share Index File', scope.files['paths']['ticker_index'], 'path_ticker_index', diff_col_size )
	three_cols( 'Path for Website Output File', scope.files['paths']['website'], 'path_website_file', diff_col_size )
	three_cols( 'Path for Share Data File', scope.files['paths']['ticker_data'], 'path_ticker_data_file', diff_col_size )



