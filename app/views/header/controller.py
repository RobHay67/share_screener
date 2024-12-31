# A function that facilitates for each page
#  (1) loading of existing share data
#  (2) adding extra columns (ie MACD) to that share data


from app.views.header.a_page_title.controller import page_title_layer
from app.views.header.b_config.buttons import render_config_buttons
from app.views.header.c_ticker_selectors.controller import render_ticker_selectors
from app.views.header.d_ticker_files.controller import load_ticker_data
from app.views.header.f_worklist.controller import render_ticker_worklist
from app.views.header.g_quick_links.quicklinks import render_quick_links
from app.views.header.h_dfs.dataframes import render_dataframes
from app.views.header.i_search.controller import render_search_results
from app.views.header.j_ticker_name.ticker_name import render_ticker_name


def render_page_header(scope, page_title, page_icon):
	page_title_layer(scope, page_title, page_icon)		# a_
	if scope.users['logged_in']:
		render_config_buttons(scope)					# b_
		render_ticker_selectors(scope)					# c_
		load_ticker_data(scope)							# d_
		render_ticker_worklist(scope)					# f_
		render_quick_links(scope)						# g_
		render_dataframes(scope)						# h_
		render_search_results(scope)					# i_
		render_ticker_name(scope)						# j_



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
