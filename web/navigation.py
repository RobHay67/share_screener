
import streamlit as st


from scope.render import welcome_page

from index.render import index_page
from tickers.render import ticker_data_files, ticker_list
from scope.render import scope_page
from analysis.render import multi_tickers_page
from analysis.render import single_ticker_page
from analysis.render import intraday_page  
from analysis.render import volume_page
from analysis.render import research_page  



def render_current_page(page):
	print( 'Rendering > ', page)
	page_render_map = {
						'initial_load'		:welcome_page,

						'ticker_index'		:index_page,
						'ticker_list'		:ticker_list,
						'share_data_files'	:ticker_data_files,
						'scope'				:scope_page,

						'analysis_multi'	:multi_tickers_page,
						'single_analysis'	:single_ticker_page,
						'intraday_analysis'	:intraday_page,
						'volume'			:volume_page,
						'research'			:research_page,

					}

	if page in list(page_render_map.keys()):
		page_render_map[page](st.session_state)
	else:
		st.warning( ('No Page yet selected > ' + page) )


# Helper - stores the selected page from the sidebar so we stay where we are on re-renders
def set_page(page:str):
	st.session_state.display_page = page




