# A function that handles all of the data loading

from partials.ticker_loader.schema import column_layout_schema
from partials.ticker_selectors.selectors import render_ticker_selectors
from partials.ticker_loader.ticker_name import render_ticker_name

from tickers.refresh_app_data import refresh_app_df_and_columns
from tickers.load.controller import load_tickers

from widgets.clear import clear_messages_button
from widgets.dataframe import dataframe_button

from partials.reports.dfs import render_ticker_dfs
from partials.reports.dfs import render_chart_dfs
from partials.reports.dfs import render_trial_dfs


from partials.ticker_loader.worklist import render_worklist
from partials.ticker_loader.worklist import render_errors


def render_ticker_loader(scope):
	
	show_chart_dfs = False
	show_trial_dfs = False

	column_layout_schema(scope)

	we_have_selected_tickers = render_ticker_selectors(scope)

	if we_have_selected_tickers:
		
		render_worklist(scope)
		
		clear_messages_button(scope)

		load_tickers(scope)

		render_errors(scope)

		render_ticker_name(scope)
		
		refresh_app_df_and_columns(scope)

		# Render buttons that allow the use to display or remove further informaiton

		with scope.col4: 
			show_ticker_files = dataframe_button(scope, 'tickers')

		if scope.apps['display_app'] == 'screener':
			with scope.col4: show_trial_dfs = dataframe_button(scope, 'trials')
		else:
			with scope.col4: show_chart_dfs = dataframe_button(scope, 'charts')
		
		# Render selected information
		if show_ticker_files: render_ticker_dfs(scope)

		if show_chart_dfs: render_chart_dfs(scope)
		
		if show_trial_dfs: render_trial_dfs(scope)
		


