
# A function that facilitates
#  (1) loading of exisiting share data
#  (2) adding extra columns (ie MACD) to that share data





import streamlit as st

from apps.app_header.app_title import render_app_title
from apps.app_header.selectors import render_ticker_selectors
from apps.app_header.ticker_data import render_ticker_data_ohlcv

# from apps.app_header.load import load_tickers
from apps.app_header.refresh_data import refresh_app_df_and_columns
from apps.app_header.navigation import render_quick_links
from apps.app_header.ticker_data import render_page_data
from apps.app_header.extra_data import render_dataframes


from apps.app_header.ticker_name import render_ticker_name
from apps.app_header.extra_data import render_config


# ==============================================================
# App Header - Layout
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



def render_app_header(scope, title):
	
	render_app_title(scope, title)

	render_config(scope)

	render_ticker_selectors(scope)

	render_ticker_data_ohlcv(scope)

	render_dataframes(scope)

	
	# we_have_selected_tickers = render_ticker_selectors(scope)

	# if we_have_selected_tickers:
		
	# 	load_tickers(scope)

	# 	refresh_app_df_and_columns(scope)

	# 	render_quick_links(scope)

	# 	render_ticker_data(scope)

	# 	render_ticker_name(scope)



		



