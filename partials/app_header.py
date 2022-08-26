
# A function that handles all of the data loading and column adding for the current App
import streamlit as st
import os

from partials.ticker_selectors.selectors import render_ticker_selectors

from partials.app_worklist import render_worklist, render_errors
from widgets.dataframe import dataframe_button
from widgets.clear import clear_messages_button

from partials.ticker_name import render_ticker_name
from partials.reports.dfs import render_ticker_dfs
from partials.reports.dfs import render_chart_dfs
from partials.reports.dfs import render_trial_dfs


from files.path import path_for_ticker_file
from tickers.load import load_ticker
from tickers.cache import cache_ticker_data
from tickers.events.missing_local_file import missing_file_event
from tickers.events.add_ticker import add_ticker_event


def render_app_header(scope, title):

	# App Report Options (default to off)
	app = scope.apps['display_app']
	show_ticker_dfs = False
	show_chart_dfs = False
	show_trial_dfs = False

	# Render App Title
	col1,col2 = st.columns([6,8])
	with col1:st.header(title)
	
	we_have_selected_tickers = render_ticker_selectors(scope)

	if we_have_selected_tickers:		
		
		load_tickers(scope)

		refresh_app_df_and_columns(scope) # iterate through worklist

		col1,col2,col3,col4,col5 = st.columns([3.0, 3.0, 2.0, 2.0, 2.0])

		# Render Data Status - whats loaded - what has load or download errors
		with col1:
			render_worklist(scope)
		with col2:
			render_errors(scope)

		# Render buttons that allow the use to display or remove further informaiton
		with col3: show_ticker_dfs = dataframe_button(scope, 'tickers')

		if scope.apps['display_app'] == 'screener':
			with col4: show_trial_dfs = dataframe_button(scope, 'trials')
		else:
			with col4: show_chart_dfs = dataframe_button(scope, 'charts')
		
		with col5: clear_messages_button(scope)

		render_ticker_name(scope)

		# Render selected information
		if show_ticker_dfs: render_ticker_dfs(scope)

		if show_chart_dfs: render_chart_dfs(scope)
		
		if show_trial_dfs: render_trial_dfs(scope)
		



# ==============================================================
# App Header - Layout
# ==============================================================
# 			------------------------------------------------------------------------------------------------------------------------
#           ....x....1....x....2....x....3....x....4....x....5....x....6....x....7....x....8....x....9....x....0....x....1....x....2
# selectors | tickers_selector | industry_selector | Market_selectors  |              Search                   | Download Button   |
# data      |      work_list             |         error_list          |  ticker_dfs       |    app_dfs        | Clear Msg Button  |
# name      |                      Ticker_Name                         |  Price            |    Volume         | Ticker Date_Range |
# 			------------------------------------------------------------------------------------------------------------------------
# col1,col2,col3,col4,col5 = st.columns([2.0, 3.0, 2.0, 3.0, 2.0])
# col1,col2,col3,col4,col5 = st.columns([3.0, 3.0, 2.0, 2.0, 2.0])
# col1,col2,col3,col4      = st.columns([6.0, 2.0, 2.0, 2.0])
# ==============================================================






# ==============================================================
# Load ticker controller here so we can render a progress bar
# on this function which can be time consuming
# ==============================================================

def load_tickers(scope):
	app = scope.apps['display_app']
	worklist = scope.apps[app]['worklist']
	no_of_tickers = len(worklist)
	already_loaded_list = scope.apps[app]['mined_tickers']
	added_progress_bar = False

	for counter, ticker in enumerate(worklist):
		if ticker not in scope.missing_tickers['local']:
			if ticker not in already_loaded_list:
				# this is the first place i might need a bar
				if added_progress_bar==False:
					col1,col2 = st.columns([2,10])
					with col1:st.write('Loading Tickers')
					with col2:my_bar = st.progress(0)
					added_progress_bar = True
				poc = int(((counter+1) / no_of_tickers ) * 100)
				my_bar.progress(poc)

				path_for_ticker_file(scope, ticker )
				# Check that a local file is available to load
				if os.path.exists( scope.files['paths']['ticker_data'] ):
					ticker_data = load_ticker(scope, ticker )
					add_ticker_event(scope, ticker)
					cache_ticker_data(scope, ticker, ticker_data)
				else:
					# The expected Local file is not available
					missing_file_event(scope, ticker)		

	if counter+1 == no_of_tickers:
		if added_progress_bar == True:
			my_bar.progress(100)





# ==============================================================
# The primary code to 
# - refresh the App df
# - Refresh specific df columns 
# ==============================================================


def refresh_app_df_and_columns(scope):

	app 				= scope.apps['display_app']
	worklist 			= scope.apps[app]['worklist']
	no_of_tickers		= len(worklist)
	app_row_limit 		= int(scope.apps['row_limit'])

	# Add Message Bar
	col1,col2 = st.columns([2,10])
	with col1:st.write('Data Refresh')
	with col2:my_bar = st.progress(0)

	for counter, ticker in enumerate(worklist):
		poc = int(((counter+1) / no_of_tickers ) * 100)
		my_bar.progress(poc)

		# Ensure data available for this ticker (function will fail if data is not available) 
		if ticker in list(scope.tickers.keys()): 
			
			# -------------------------------------------------------------------
			# Replace the App df if requested
			# -------------------------------------------------------------------
			if scope.tickers[ticker][app]['replace_df'] == True:
				ticker_df = scope.tickers[ticker]['df'].copy()
				ticker_df = ticker_df.head(app_row_limit) 				# limit no of rows for the APP df (speeds up app rendering)				
				scope.tickers[ticker][app]['df'] = ticker_df			# Cache the ticker dataframe to be mined by this app

				# add ticker to the mined_ticker list
				if ticker not in scope.apps[app]['mined_tickers']:
					scope.apps[app]['mined_tickers'].append(ticker)
				
				# Set the status to false to prevent refreshing unnecesarily	
				scope.tickers[ticker][app]['replace_df'] = False

			# -------------------------------------------------------------------
			# Replace specific columns in the app df if requested
			# -------------------------------------------------------------------
			type_of_column_adder = scope.tickers[ticker][app]['type_col_adder']
			if type_of_column_adder != None:			
				# Some apps do not have any column adders
				for column_adder, status in scope.tickers[ticker][app]['column_adders'].items():
					if status == True:	
						# Only replace the columns if requested to do so for this column adder
						ticker_df = scope.tickers[ticker][app]['df']
						# Call the column adding function for this column_adder
						scope[type_of_column_adder][column_adder]['add_columns']['function'](scope, column_adder, ticker, ticker_df)
						# Set the status to false to prevent refreshing unnecesarily
						scope.tickers[ticker][app]['column_adders'][column_adder] = False
