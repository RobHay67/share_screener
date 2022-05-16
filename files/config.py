import os

import streamlit as st
from config.results.three_cols import three_cols


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
	scope.files['paths']['users'] = os.path.join(scope.files['folders']['files'], 'users.json')
	scope.files['paths']['ticker_index'] = os.path.join(scope.files['folders']['files'], 'ticker_index.csv')
	scope.files['paths']['ticker_data'] = 'not yet set'
	scope.files['paths']['website'] = os.path.join(scope.files['folders']['website'], 'strategy_results.json')




