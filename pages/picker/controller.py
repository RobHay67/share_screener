# A single function that handles all of the data loading

from pages.picker.load_screen import column_structure_for_page
from pages.picker.selectors import render_selectors

from pages.data.renew import renew_pages_dfs

from data.tickers.load import load_tickers
from data.tickers.download import download_tickers
from data.tickers.view.dataframes import view_ticker_data_files


from pages.picker.buttons.download import download_button
from pages.picker.buttons.clear_message import clear_messages_button
from pages.picker.buttons.ticker_file import ticker_file_button
from pages.picker.buttons.screener_dfs import screener_dfs_button
from pages.picker.buttons.chart_dfs import chart_dfs_button

# TODO - do these need to be seperate??? maybe a single function should handle both
from pages.view.dataframes import view_screener_dfs
from pages.view.dataframes import view_chart_dfs



def render_ticker_picker(scope):

	column_structure_for_page(scope)

	selected_tickers_status = render_selectors(scope)

	if selected_tickers_status:

		page = scope.pages['display_page']

		with scope.col1: download_new_ticker_data = download_button(scope)		
		with scope.col6: clear_messages_button(scope)

		# AUTO load whatever ticker data we have	
		load_tickers(scope)
		
		if download_new_ticker_data: download_tickers(scope)

		renew_pages_dfs(scope)  

		with scope.col5: show_ticker_files = ticker_file_button(scope)

		if page == 'screener':
			show_chart_dfs = False
			with scope.col5: show_screener_dfs = screener_dfs_button(scope)
		else:
			show_screener_dfs = False
			with scope.col5: show_chart_dfs = chart_dfs_button(scope)
		
		if show_ticker_files: view_ticker_data_files(scope, page)
		if show_screener_dfs: view_screener_dfs(scope, page)
		if show_chart_dfs: view_chart_dfs(scope, page)



	# import streamlit as st
	# page = scope.pages['display_page']
	
	# ticker_list = scope.pages[page]['ticker_list']

	# st.write(ticker_list)
	# st.write(scope.data['download']['industries'])



