# A single function that handles all of the data loading

from pages.picker.load_screen import set_cols

from data.tickers.load import load_tickers
from data.tickers.download import download_tickers
from data.tickers.view.dataframes import view_ticker_data_files

from pages.data.renew import update_page_dfs

from pages.picker.which_tickers import ticker_selectors
from pages.picker.buttons.download import download_button
from pages.picker.buttons.clear_message import clear_messages_button
from pages.picker.buttons.ticker_file import ticker_file_button
from pages.picker.buttons.screener_dfs import screener_dfs_button
from pages.picker.buttons.chart_dfs import chart_dfs_button

from pages.view.dataframes import view_screener_dfs
from pages.view.dataframes import view_chart_dfs



def render_ticker_picker(scope):

	page = scope.pages['display_page']

	set_cols(scope)

	selected_tickers_so_lets_load = ticker_selectors(scope)

	if selected_tickers_so_lets_load:
		with scope.col1: download_new_data = download_button(scope)		
		with scope.col6: clear_messages_button(scope)

		# AUTO load whatever ticker data we have	
		load_tickers(scope)
		
		if download_new_data: 
			download_tickers(scope)

		update_page_dfs(scope)  
		#TODO this is where we used to update the columns (as per the update_page_dfs)
		print('Rob - we need to have an update columns function - copy from the a_old_update_page_dfs module')


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





