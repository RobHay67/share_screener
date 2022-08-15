# A function that handles all of the data loading

from partials.ticker_loader.schema import column_layout_schema
from partials.ticker_selectors.selectors import render_ticker_selectors
from partials.ticker_loader.ticker_name import render_ticker_name

from tickers.refresh_app_data import refresh_app_df_and_columns
from tickers.load_controller import load_tickers

from partials.messages import clear_messages_button
from partials.dfs import dfs_button
from partials.dfs import render_ticker_dfs
from partials.dfs import render_chart_dfs
from partials.dfs import render_trial_dfs





def render_ticker_loader(scope):
	
	show_chart_dfs = False
	show_trial_dfs = False

	column_layout_schema(scope)

	we_have_selected_tickers = render_ticker_selectors(scope)

	if we_have_selected_tickers:
		
		load_tickers(scope)

		render_ticker_name(scope)
		
		refresh_app_df_and_columns(scope)

		# Render buttons that allow the use to display or remove further informaiton
		clear_messages_button(scope)

		with scope.col4: 
			show_ticker_files = dfs_button(scope, 'tickers')

		if scope.apps['display_app'] == 'screener':
			with scope.col4: show_trial_dfs = dfs_button(scope, 'trials')
		else:
			with scope.col4: show_chart_dfs = dfs_button(scope, 'charts')
		
		# Render selected information
		if show_ticker_files: render_ticker_dfs(scope)

		if show_chart_dfs: render_chart_dfs(scope)
		
		if show_trial_dfs: render_trial_dfs(scope)
		


