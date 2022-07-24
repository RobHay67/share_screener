# A single function that handles all of the data loading

from apps.ticker_loader.layout import column_structure_for_page
from apps.ticker_loader.selectors import render_ticker_selectors

from apps.data.replace import replace_dfs
from apps.data.replace import replace_cols

from data.tickers.load import load_tickers
from data.tickers.view.dataframes import view_ticker_files


# from apps.ticker_loader.buttons.download import download_button
from apps.ticker_loader.buttons.clear_message import clear_messages_button
from apps.ticker_loader.buttons.ticker_file import ticker_file_button
from apps.ticker_loader.buttons.screener_dfs import screener_dfs_button
from apps.ticker_loader.buttons.chart_dfs import chart_dfs_button

# TODO - do these need to be seperate??? maybe a single function should handle both
from apps.ticker_loader.dataframes import view_screener_dfs
from apps.ticker_loader.dataframes import view_chart_dfs


def render_ticker_loader(scope):

	column_structure_for_page(scope)

	selected_tickers_status = render_ticker_selectors(scope)

	if selected_tickers_status:

		page = scope.pages['display_page']

		with scope.col6: clear_messages_button(scope)

		# AUTO load whatever ticker data we have	
		load_tickers(scope)
		
		with scope.col5: show_ticker_files = ticker_file_button(scope)

		replace_dfs(scope)
		replace_cols(scope)

		if page == 'screener':
			show_chart_dfs = False
			with scope.col5: show_screener_dfs = screener_dfs_button(scope)
		else:
			show_screener_dfs = False
			with scope.col5: show_chart_dfs = chart_dfs_button(scope)
		
		if show_ticker_files: view_ticker_files(scope)
		if show_screener_dfs: view_screener_dfs(scope)
		if show_chart_dfs: view_chart_dfs(scope)




