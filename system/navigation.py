
import streamlit as st


from system.scope import welcome_page

# from index.controller import index_page
# from ticker.render import ticker_data_files, ticker_list
from system.scope import scope_page
from analysis.controller import multi_tickers_page
from analysis.controller import single_ticker_page
from analysis.controller import intraday_page  
from analysis.controller import volume_page
from analysis.controller import research_page  



def render_current_page(page):
	# print( 'Rendering > ', page)
	page_render_map = {
						'initial_load'	:welcome_page,
						'scope'			:scope_page,

						'single'		:single_ticker_page,
						'intraday'		:intraday_page,
						'volume'		:volume_page,
						'research'		:research_page,
						'multi'			:multi_tickers_page,

					}

	if page in list(page_render_map.keys()):
		page_render_map[page](st.session_state)
	else:
		st.warning( ('No Page yet selected > ' + page) )


# Helper - stores the selected page from the sidebar so we stay where we are on re-renders
def set_page(page:str):
	st.session_state.display_page = page




