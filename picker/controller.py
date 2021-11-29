# A single function that handles all of the data loading

from picker.view.load_screen import set_cols

from ticker.load import load_tickers
from ticker.download import download_tickers
from ticker.view.dataframes import view_ticker_data_files

from analysis.model.analysis_df import create_analysis_df
from analysis.view.dataframes import view_analysis_dfs
from charts.model.chart_df import create_chart_df
from charts.view.dataframes import view_chart_dfs

from picker.helpers.which_tickers import ticker_selectors
from picker.buttons.download import download_button
from picker.buttons.clear_message import clear_messages_button
from picker.buttons.ticker_file import ticker_file_button
from picker.buttons.analysis_dfs import analysis_dfs_button
from picker.buttons.chart_dfs import chart_dfs_button



def ticker_picker(scope, page):

	set_cols(scope, page)

	we_are_loading, ticker_list = ticker_selectors(scope, page)

	if we_are_loading:
		with scope.col1: download_new_data = download_button(scope)		
		with scope.col6: clear_messages_button(scope)

		load_tickers(scope, ticker_list)													# AUTO load whatever ticker data we have	
		if download_new_data: download_tickers(scope)
		create_analysis_df(scope, ticker_list)												# Code only runs if refresh_analysis_df set to TRUE
		create_chart_df(scope, ticker_list)													# Code only runs if refresh_chart_df set to TRUE

		with scope.col5: show_ticker_files = ticker_file_button(scope, ticker_list)
		with scope.col5: show_analysis_dfs = analysis_dfs_button(scope, page, ticker_list)
		with scope.col5: show_chart_dfs    = chart_dfs_button(scope, page, ticker_list)
		
		if show_ticker_files	: view_ticker_data_files(scope, page)
		if show_analysis_dfs	: view_analysis_dfs(scope, page)
		if show_chart_dfs		: view_chart_dfs(scope, page)

