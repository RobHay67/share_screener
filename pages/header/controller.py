# A function that facilitates
#  (1) loading of existing share data
#  (2) adding extra columns (ie MACD) to that share data


import streamlit as st

from pages.sidebar.sidebar import render_sidebar
from pages.header.page_title import page_title_layer
from pages.header.page_config import render_config_and_settings
from pages.header.selectors import selectors_layer
from pages.header.ticker_files import ticker_files_layer
from pages.header.add_columns import add_cols_to_df_layer
from pages.header.worklist import ticker_worklist_layer
from pages.header.quicklinks import quick_links_layer
from pages.header.dataframes import render_dataframes
from pages.header.ticker_name import selected_ticker_name_layer
from pages.header.search import render_search_results


def render_app_header(scope, page_title, page_icon):
	
	render_sidebar(scope)

	page_title_layer(scope, page_title, page_icon)

	if scope.user_logged_in:
	
		render_config_and_settings(scope)

		selectors_layer(scope)
		ticker_files_layer(scope)
		add_cols_to_df_layer(scope)
		ticker_worklist_layer(scope)
		quick_links_layer(scope)

		render_dataframes(scope)

		render_search_results(scope)

		selected_ticker_name_layer(scope)



	

	



		



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
