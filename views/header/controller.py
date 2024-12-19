# A function that facilitates for each page
#  (1) loading of existing share data
#  (2) adding extra columns (ie MACD) to that share data




from views.header.page_title.controller import page_title_layer
from views.header.config_buttons import render_config_buttons
from views.header.ticker_selectors.controller import render_ticker_selectors
from views.header.ticker_files.controller import load_ticker_files
from views.header.add_columns.controller import progress_adding_columns_to_data
from views.header.worklist.controller import render_ticker_worklist
from views.header.quicklinks import render_quick_links
from views.header.dataframes import render_dataframes
from views.header.ticker_name import render_ticker_name
from views.header.search.controller import render_search_results


def render_page_header(scope, page_title, page_icon):
	
	page_title_layer(scope, page_title, page_icon)

	if scope.users['logged_in']:
		
		# import streamlit as st
		# page = scope.pages['display']
		# col1,col2 = st.columns([2.0,10.0])  #12
		# with col1:
		# 	st.write('Worklist')
		# 	st.write(scope.pages[page]['worklist'])
			
		# with col2:
		# 	st.write('download_these_industries')
		# 	st.write(scope.yf['download_these_industries'])



		render_config_buttons(scope)
		
		
		render_ticker_selectors(scope)
		load_ticker_files(scope)
		progress_adding_columns_to_data(scope)
		render_ticker_worklist(scope)
		render_quick_links(scope)
		render_dataframes(scope)
		render_search_results(scope)
		render_ticker_name(scope)



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
