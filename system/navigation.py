
import streamlit as st


from system.project import view_project_welcome
from system.scope import view_scope
from system.user import view_user
from system.chart import view_chart
from analysis.controller import single_ticker_page, intraday_page, volume_page, research_page, multi_tickers_page


def view_current_page(page):
	# print( 'Rendering > ', page)
	page_view_map = {
						'initial_load'	:view_project_welcome,

						'charts'		:view_chart,
						'user'			:view_user,
						'single'		:single_ticker_page,
						'intraday'		:intraday_page,
						'volume'		:volume_page,
						'research'		:research_page,
						'multi'			:multi_tickers_page,
						'scope'			:view_scope,
					}

	if page in list(page_view_map.keys()):
		page_view_map[page](st.session_state)
	else:
		st.warning( ('No Page yet selected > ' + page) )


# Helper - stores the selected page from the sidebar so we stay where we are on re-renders
def set_page(page:str):
	st.session_state.display_page = page




