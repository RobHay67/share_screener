
# A function that handles all of the data loading
import streamlit as st


from partials.schema import column_layout_schema
from partials.ticker_selectors.selectors import render_ticker_selectors
from partials.ticker_name import render_ticker_name

from tickers.events.refresh_app_data import refresh_app_df_and_columns
from tickers.load.controller import load_tickers

from widgets.clear import clear_messages_button
from widgets.dataframe import dataframe_button

from partials.reports.dfs import render_ticker_dfs
from partials.reports.dfs import render_chart_dfs
from partials.reports.dfs import render_trial_dfs


from partials.app_worklist import render_worklist
from partials.app_worklist import render_errors

def render_app_header(scope, title):

	col1,col2 = st.columns([6,8])
	
	with col1:
		st.header(title)



# def render_ticker_loader(scope):
	
	show_chart_dfs = False
	show_trial_dfs = False

	# column_layout_schema(scope, row=1)

	we_have_selected_tickers = render_ticker_selectors(scope)

	if we_have_selected_tickers:
		
		# clear_messages_button(scope)

		load_tickers(scope)

		
		refresh_app_df_and_columns(scope)

		col1,col2,col3,col4      = st.columns([6.0, 2.0, 2.0, 2.0])

		with col1:
			render_worklist(scope)
			render_errors(scope)


		# Render buttons that allow the use to display or remove further informaiton
		with col2: 
			show_ticker_files = dataframe_button(scope, 'tickers')

		if scope.apps['display_app'] == 'screener':
			with col3: show_trial_dfs = dataframe_button(scope, 'trials')
		else:
			with col3: show_chart_dfs = dataframe_button(scope, 'charts')
		
		with col4:
			clear_messages_button(scope)


		render_ticker_name(scope)

			


		# Render selected information
		if show_ticker_files: render_ticker_dfs(scope)

		if show_chart_dfs: render_chart_dfs(scope)
		
		if show_trial_dfs: render_trial_dfs(scope)
		


