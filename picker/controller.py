# A single function that handles all of the data loading

from picker.view.load_screen import set_cols

from tickers.load import load_tickers
from tickers.download import download_tickers
from tickers.view.dataframes import view_ticker_data_files

from pages.model.screener_dfs import update_screener_dfs
from pages.model.screener_dfs import update_screener_metrics

from pages.model.chart_df import update_chart_dfs
from pages.model.chart_df import update_chart_metrics

from pages.view.dataframes import view_screener_dfs
from pages.view.dataframes import view_chart_dfs

from picker.helpers.which_tickers import ticker_selectors
from picker.buttons.download import download_button
from picker.buttons.clear_message import clear_messages_button
from picker.buttons.ticker_file import ticker_file_button
from picker.buttons.screener_dfs import screener_dfs_button
from picker.buttons.chart_dfs import chart_dfs_button



def ticker_picker(scope, page):

	set_cols(scope, page)

	selected_tickers_so_lets_load, ticker_list = ticker_selectors(scope, page)

	if selected_tickers_so_lets_load:
		with scope.col1: download_new_data = download_button(scope)		
		with scope.col6: clear_messages_button(scope)

		# TODO - why is the ticker list not being stored for each page??? the function would not need to return it then

		load_tickers(scope, ticker_list)													# AUTO load whatever ticker data we have	
		if download_new_data: download_tickers(scope)
		update_screener_dfs(scope, ticker_list)												# Code only runs if refresh_ticker_data set to TRUE
		update_screener_metrics(scope, ticker_list)											# Code only runs if refresh_metrics 	set to TRUE		
		update_chart_dfs(scope, ticker_list)												# Code only runs if refresh_ticker_data set to TRUE
		update_chart_metrics(scope, ticker_list)											# Code only runs if refresh_metrics 	set to TRUE		

		with scope.col5: show_ticker_files = ticker_file_button(scope, ticker_list)

		if page == 'screener':
			with scope.col5: show_screener_dfs = screener_dfs_button(scope, page, ticker_list)
			show_chart_dfs = False
		else:
			with scope.col5: show_chart_dfs = chart_dfs_button(scope, page, ticker_list)
			show_screener_dfs = False
		
		if show_ticker_files	: view_ticker_data_files(scope, page)
		if show_screener_dfs	: view_screener_dfs(scope, page)
		if show_chart_dfs		: view_chart_dfs(scope, page)

