
# A function that handles all of the data loading and column adding for the current App
import streamlit as st

from partials.app_header.selectors import render_ticker_selectors
from partials.app_header.load import load_tickers
from partials.app_header.refresh_data import refresh_app_df_and_columns
from partials.app_header.navigation import render_quick_links
from partials.app_header.page_data import render_page_data
from partials.app_header.extra_data import render_optional_information


from partials.app_header.ticker_name import render_ticker_name



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

	# Render Page Title
	col1,col2,col3 = st.columns([8,2,2])
	with col1:
		st.subheader(title)
		# st.write('This is the header')
	with col2:
		st.write('Test this')


	# TODO - the title probably needs to be in its own module as well
	print('Working onn this part now rob')
	
	we_have_selected_tickers = render_ticker_selectors(scope)

	if we_have_selected_tickers:		
		
		load_tickers(scope)

		refresh_app_df_and_columns(scope)

		render_quick_links(scope)

		render_page_data(scope)

		render_ticker_name(scope)

		render_optional_information(scope)


		



