# A single function that handles all of the data loading

from pages.picker.view.load_screen import set_cols

from data.tickers.load import load_tickers
from data.tickers.download import download_tickers
from data.tickers.view.dataframes import view_ticker_data_files

from pages.model.screener_dfs import update_screener_dfs
from pages.model.screener_dfs import update_screener_metrics

from pages.model.chart_dfs import update_chart_dfs
from pages.model.chart_dfs import update_chart_metrics

from pages.view.dataframes import view_screener_dfs
from pages.view.dataframes import view_chart_dfs

from pages.picker.helpers.which_tickers import ticker_selectors
from pages.picker.buttons.download import download_button
from pages.picker.buttons.clear_message import clear_messages_button
from pages.picker.buttons.ticker_file import ticker_file_button
from pages.picker.buttons.screener_dfs import screener_dfs_button
from pages.picker.buttons.chart_dfs import chart_dfs_button


def page_report(scope, heading ):

	print('='*100)
	print(heading.upper())
	print( '-'*100)
	print( 'ohlcv'.upper())
	for page in scope.pages['page_list']:
		print(page.upper())
		for ticker in scope.pages[page]['refresh_df']['ohlcv'].keys():
			print( ('  - ' + ticker).ljust(10), ' - ', scope.pages[page]['refresh_df']['ohlcv'][ticker] )
	print('-'*100)
	print( 'test'.upper())
	for page in scope.pages['page_list']:
		print(page.upper())
		for ticker in scope.pages[page]['refresh_df']['tests'].keys():
			print( ('  - ' + ticker).ljust(10), ' - ', scope.pages[page]['refresh_df']['tests'][ticker] )
	print('-'*100)
	print( 'chart'.upper())
	for page in scope.pages['page_list']:
		print(page.upper())
		for ticker in scope.pages[page]['refresh_df']['charts'].keys():
			print( ('  - ' + ticker).ljust(10), ' - ', scope.pages[page]['refresh_df']['charts'][ticker] )
	print('='*100)





def render_ticker_picker(scope):

	page = scope.pages['display_page']

	set_cols(scope, page)

	selected_tickers_so_lets_load = ticker_selectors(scope, page)

	if selected_tickers_so_lets_load:
		with scope.col1: download_new_data = download_button(scope)		
		with scope.col6: clear_messages_button(scope)

		load_tickers(scope)														# AUTO load whatever ticker data we have	
		
		if download_new_data: 
			download_tickers(scope)

		update_screener_dfs(scope)												# Code only runs if ohlcv  set to TRUE
		update_screener_metrics(scope)											# Code only runs if test set to TRUE		
		update_chart_dfs(scope)													# Code only runs if ohlcv  set to TRUE
		update_chart_metrics(scope)												# Code only runs if test set to TRUE		

		with scope.col5: show_ticker_files = ticker_file_button(scope)

		if page == 'screener':
			with scope.col5: show_screener_dfs = screener_dfs_button(scope)
			show_chart_dfs = False
		else:
			with scope.col5: show_chart_dfs = chart_dfs_button(scope)
			show_screener_dfs = False
		
		if show_ticker_files	: view_ticker_data_files(scope, page)
		if show_screener_dfs	: view_screener_dfs(scope, page)
		if show_chart_dfs		: view_chart_dfs(scope, page)





