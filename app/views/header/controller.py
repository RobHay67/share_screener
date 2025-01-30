from app.views.header.a_page_title.router import page_title_layer
from app.views.header.router_show_settings import router_show_settings
from app.views.header.router_show_config import router_show_config
from app.views.header.c_ticker_selectors.router_ticker_selectors import router_show_ticker_selectors
from app.views.header.d_ticker_files.controller import show_ticker_load_and_col_adding
from app.views.header.f_worklists.controller import show_worklist_dropdowns
from app.views.header.show_quicklinks import router_show_quick_links
from app.views.header.show_dataframes import show_dataframes
from app.views.header.i_search.show_search_results import show_search_results
from app.views.header.show_ticker_name import show_ticker_name





def show_page_header(scope):
	page_title_layer(scope)								# a_
	if scope.users['logged_in']:
		# Levels at the top of the page
		router_show_settings(scope)						# b_
		router_show_config(scope)						# b_
		router_show_ticker_selectors(scope)				# c_
		show_ticker_load_and_col_adding(scope)			# d_
		show_worklist_dropdowns(scope)					# f_
		# Optional items to show as requested
		router_show_quick_links(scope)						
		show_dataframes(scope)		
		show_search_results(scope)						# i_
		show_ticker_name(scope)


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


