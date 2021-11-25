# A single function that handles all of the data loading

from ticker.views.load_screen import set_cols
from ticker.helpers.which_tickers import ticker_selectors
from ticker.views.buttons import download_button, clear_messages_button, ticker_file_button, analysis_dfs_button, chart_dfs_button
from ticker.model.load import load_tickers
from analysis.model.analysis_df import create_analysis_df
from charts.model.chart_df import create_chart_df
from ticker.downloader import download_tickers
from ticker.views.dataframes import view_ticker_data_files
from analysis.views.dataframes import view_analysis_dfs
from charts.views.dataframes import view_chart_dfs
from ticker.views.scope import set_download_days
from analysis.views.scope import set_analysis_row_limit


def ticker_loader(scope, page):

	set_cols(scope, page)

	we_are_loading, ticker_list = ticker_selectors(scope, page)

	if we_are_loading:
		with scope.col1: download_new_data = download_button(scope)		
		with scope.col4: set_download_days(scope)
		with scope.col4: set_analysis_row_limit(scope)
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

