import logging
from page.header.router_page_title import page_title
from page.header.router_show_clicked_settings import router_show_clicked_settings
from page.header.router_show_selected_config import router_show_selected_config
from page.header.router_ticker_selectors import ticker_selectors
from page.header.c_ticker_files.controller import router_progress_bars
from page.header.d_worklists.controller import worklist_selectors
from page.header.show_quicklinks import add_quick_links
from tickers.scope.view_dataframes import add_page_dataframes
from page.header.i_search_results.search_company_by_name import search_company_by_name
from page.header.add_ticker_name import add_ticker_name
from page.header.router_show_active_trial_or_test import router_show_active_trial_or_test
from trials.views.verdicts.router_show_verdicts import router_show_verdicts
from trials.views.fliss_simple import show_fliss_simple_strategy

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
	show_active_trial_or_chart = False

	# Determine what is to be be shown / displayed
	if (scope.page[page]['show']['trials'] == True or
		scope.page[page]['show']['strategy'] == True or
		scope.page[page]['show']['charts'] == True or
		scope.page[page]['show']['overlays'] == True
		): show_settings=True
	if page != 'screener':
		ticker = scope.page[page]['selectors']['ticker']
		if ticker != None:
			show_quick_links = True
			show_ticker_name = True
	if scope.page[page]['show']['config'] != None:show_config=True
	if scope.page[page]['show']['ticker_file'] != 'Show/Hide Data':show_ticker_files = True
	if len(scope.page[page]['search_results']) > 0:show_search_results=True
	if scope.page[page]['show']['active_trial_or_chart']:show_active_trial_or_chart=True

	page_title(scope)											# a_
	if scope.users['logged_in']:
		ticker_selectors(scope)									# b_
		router_progress_bars(scope)									# c_
		worklist_selectors(scope)								# d_
		# show Settings
		if show_settings:router_show_clicked_settings(scope)	# 
		# Optional items to show as requested
		if show_config:router_show_selected_config(scope)		# 
		if show_quick_links:add_quick_links(scope)	
		if show_ticker_files: add_page_dataframes(scope)
		if show_search_results:search_company_by_name(scope)	# i_
		if show_ticker_name:add_ticker_name(scope)
		if show_active_trial_or_chart:router_show_active_trial_or_test(scope)
		
		if page=='screener':
			if len(scope.page[page]['list_loaded_tickers'])>0:
				router_show_verdicts(scope)
				show_fliss_simple_strategy(scope)
				logging.critical('remove show_fliss_simple_strategy when Strategy can be managed in settings')



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


