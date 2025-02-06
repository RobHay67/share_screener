import logging
from page.header.router_page_title import row_page_title
from page.header.router_show_requested_settings import router_show_requested_settings
from page.header.router_show_requested_config import router_show_requested_config
from page.header.router_ticker_selectors import row_ticker_selectors
from page.header.c_ticker_files.controller import row_progress_bars
from page.header.d_worklists.controller import row_page_list_dropdowns
from page.header.show_quicklinks import add_quick_links
from tickers.scope.view.dataframes import add_page_dataframes
from page.header.i_search_results.add_search_results import add_search_results
from page.header.add_ticker_name import add_ticker_name


def controller_page_header(scope):
	logging.info("controller_page_header")
	page = scope.display['page']

	# default show status for optional display items
	show_settings=False
	show_config=False
	show_quick_links = False
	show_ticker_files = False
	show_search_results = False
	show_ticker_name = False

	if (scope.page[page]['show']['trials'] == True or
		scope.page[page]['show']['strategy'] == True or
		scope.page[page]['show']['charts'] == True or
		scope.page[page]['show']['overlays'] == True
		): show_settings=True

	if scope.page[page]['show']['config'] != None:
		show_config=True

	if page != 'screener':
		ticker = scope.page[page]['selectors']['ticker']
		if ticker != 'select a ticker':
			show_quick_links = True
			show_ticker_name = True

	if scope.page[page]['show']['ticker_file'] != 'Show/Hide Data':
		show_ticker_files = True

	if len(scope.page[page]['search_results']) > 0: 
		show_search_results=True

	row_page_title(scope)						# a_
	if scope.users['logged_in']:
		row_ticker_selectors(scope)						# b_
		row_progress_bars(scope)	# c_
		row_page_list_dropdowns(scope)					# d_
		
		# show Settings
		if show_settings:router_show_requested_settings(scope)		# 
		# Optional items to show as requested
		if show_config:router_show_requested_config(scope)			# 
		if show_quick_links:add_quick_links(scope)	
		if show_ticker_files: add_page_dataframes(scope)
		if show_search_results:add_search_results(scope)	# i_
		if show_ticker_name:add_ticker_name(scope)




# ==============================================================
# page Header - Layout
# ==============================================================
# 			------------------------------------------------------------------------------------------------------------------------
#           ....x....1....x....2....x....3....x....4....x....5....x....6....x....7....x....8....x....9....x....0....x....1....x....2
# selectors | tickers_selector | industry_selector | Market_selectors  |              Search                   | Download Button   |
# data      |      work_list             |         error_list          |  ticker_dfs       |    app_dfs        | Clear Msg Button  |
# name      |                      Ticker_Name                         |  Price            |    Volume         | Ticker Date_Range |
# 			------------------------------------------------------------------------------------------------------------------------
# col1,col2,col3,col4,col5 = st.columns([2.0, 3.0, 2.0, 3.0, 2.0])
# col1,col2,col3,col4,col5 = st.columns([3.0, 3.0, 2.0, 2.0, 2.0])
# col1,col2,col3,col4      = st.columns([6.0, 2.0, 2.0, 2.0])
# ==============================================================


