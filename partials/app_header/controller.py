
# A function that handles all of the data loading and column adding for the current App
import streamlit as st

from partials.ticker_selectors.selectors import render_ticker_selectors
from partials.app_header.load import load_tickers
from partials.app_header.refresh_data import refresh_app_df_and_columns

from partials.app_worklist import render_worklist, render_errors
from widgets.dataframe import dataframe_button
from widgets.clear import clear_messages_button
from partials.ticker_name import render_ticker_name
from partials.reports.dfs import render_ticker_dfs
from partials.reports.dfs import render_chart_dfs
from partials.reports.dfs import render_trial_dfs


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
		



