# A function that handles all of the data loading

from partials.ticker_loader.schema import layout_schema
from partials.ticker_selectors.selectors import render_ticker_selectors

from tickers.refresh_app_data import refresh_app_df_and_columns
from tickers.load_controller import load_tickers

from partials.ticker_loader.buttons.clear_message import clear_messages_button
from partials.ticker_loader.buttons.ticker_file import ticker_files_button
from partials.ticker_loader.buttons.screener_dfs import screener_dfs_button
from partials.ticker_loader.buttons.chart_dfs import chart_dfs_button

from partials.dataframes.tickers import view_ticker_files
from partials.dataframes.trials import view_trials_dfs
from partials.dataframes.charts import view_chart_dfs


def render_ticker_loader(scope):

	layout_schema(scope)

	selected_tickers_status = render_ticker_selectors(scope)

	with scope.col5: 
		show_ticker_files = ticker_files_button(scope)

	if show_ticker_files: 
		view_ticker_files(scope)

	if selected_tickers_status:

		with scope.col6: 
			clear_messages_button(scope)

		# AUTO load whatever ticker data we have	
		load_tickers(scope)
		
		refresh_app_df_and_columns(scope)

		if scope.apps['display_app'] == 'screener':
			show_chart_dfs = False
			with scope.col5: 
				show_screener_dfs = screener_dfs_button(scope)
		else:
			show_screener_dfs = False
			with scope.col5: 
				show_chart_dfs = chart_dfs_button(scope)
		
		if show_screener_dfs: 
			view_trials_dfs(scope)
		if show_chart_dfs: 
			view_chart_dfs(scope)




