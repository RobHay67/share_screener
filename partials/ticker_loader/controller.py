# A function that handles all of the data loading

from partials.ticker_loader.schema import column_layout_schema
from partials.ticker_selectors.selectors import render_ticker_selectors
from partials.ticker_loader.ticker_name import render_ticker_name

from tickers.refresh_app_data import refresh_app_df_and_columns
from tickers.load_controller import load_tickers

from partials.ticker_loader.buttons.clear_message import clear_messages_button
from partials.ticker_loader.buttons.ticker_dfs import ticker_dfs_button, view_ticker_files
from partials.ticker_loader.buttons.chart_dfs import chart_dfs_button, view_chart_dfs
from partials.ticker_loader.buttons.trial_dfs import trial_dfs_button, view_trials_dfs


def render_ticker_loader(scope):
	
	show_chart_dfs = False
	show_trial_dfs = False

	column_layout_schema(scope)

	we_have_selected_tickers = render_ticker_selectors(scope)

	with scope.col4: show_ticker_files = ticker_dfs_button(scope)

	if show_ticker_files: view_ticker_files(scope)

	if we_have_selected_tickers:
		
		clear_messages_button(scope)

		load_tickers(scope)

		render_ticker_name(scope)
		
		refresh_app_df_and_columns(scope)

		if scope.apps['display_app'] == 'screener':
			with scope.col4: show_trial_dfs = trial_dfs_button(scope)
		else:
			with scope.col4: show_chart_dfs = chart_dfs_button(scope)
		
		if show_trial_dfs: view_trials_dfs(scope)
		
		if show_chart_dfs: view_chart_dfs(scope)
		



