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


def page_report(scope, heading ):

	print('='*100)
	print(heading.upper())
	print( '-'*100)
	print( 'add_ohlcv_data'.upper())
	for page in scope.pages['page_list']:
		print(page.upper())
		for ticker in scope.pages[page]['add_ohlcv_data'].keys():
			print( ('  - ' + ticker).ljust(10), ' - ', scope.pages[page]['add_ohlcv_data'][ticker] )
	print('-'*100)
	print( 'add_metric_data'.upper())
	for page in scope.pages['page_list']:
		print(page.upper())
		for ticker in scope.pages[page]['add_metric_data'].keys():
			print( ('  - ' + ticker).ljust(10), ' - ', scope.pages[page]['add_metric_data'][ticker] )
	print('-'*100)
	print( 'add_chart_data'.upper())
	for page in scope.pages['page_list']:
		print(page.upper())
		for ticker in scope.pages[page]['add_chart_data'].keys():
			print( ('  - ' + ticker).ljust(10), ' - ', scope.pages[page]['add_chart_data'][ticker] )
	print('='*100)





def ticker_picker(scope):

	page = scope.pages['display_page']
	# print ( 'scope.pages['templates']['add_chart_data'] = ', scope.pages['templates']['add_chart_data'])
	set_cols(scope, page)

	# selected_tickers_so_lets_load, ticker_list = ticker_selectors(scope, page)
	selected_tickers_so_lets_load = ticker_selectors(scope, page)

	if selected_tickers_so_lets_load:
		with scope.col1: download_new_data = download_button(scope)		
		with scope.col6: clear_messages_button(scope)

		# TODO - why is the ticker list not being stored for each page??? the function would not need to return it then

		# load_tickers(scope, ticker_list)													# AUTO load whatever ticker data we have	
		load_tickers(scope)
		if download_new_data: download_tickers(scope)

		# page_report(scope, 'BEFORE running all the updates ')

		update_screener_dfs(scope)												# Code only runs if add_ohlcv_data set to TRUE
		update_screener_metrics(scope)											# Code only runs if add_metric_data 	set to TRUE		
		update_chart_dfs(scope)												# Code only runs if add_ohlcv_data set to TRUE
		update_chart_metrics(scope)											# Code only runs if add_metric_data 	set to TRUE		

		# page_report(scope, 'AFTER running all the updates - < add_ohlcv_data > values' )

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





