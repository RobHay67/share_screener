
import streamlit as st


from home.view import view_project_welcome
from scope.view import view_scope
from scope.user.view import view_user
from analysis.charts.view import view_primary, view_secondary
from analysis.controller import single_ticker_page, intraday_page, volume_page, research_page, multi_tickers_page


def view_selected_page(page):
	# print( 'Rendering > ', page)
	page_view_map = {
						'home_page'			:view_project_welcome,
						'charts_primary'	:view_primary,
						'charts_secondary'	:view_secondary,
						'user'				:view_user,
						'single'			:single_ticker_page,
						'intraday'			:intraday_page,
						'volume'			:volume_page,
						'research'			:research_page,
						'multi'				:multi_tickers_page,
						'scope'				:view_scope,
					}

	if page in list(page_view_map.keys()):
		page_view_map[page](st.session_state)
	else:
		st.warning( ('No Page yet selected > ' + page) )



# Helper - stores the selected page from the sidebar so we stay where we are on re-renders
def store_page(page:str):
	st.session_state.display_page = page


