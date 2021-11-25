
import streamlit as st


from home.view import view_project_welcome
from scope.view import view_scope
from scope.user.view import view_user
from charts.views.primary import view_primary
from charts.views.secondary import view_secondary
from analysis.controller import single_ticker_analysis, intraday_analysis, volume_analysis, research_analysis, multi_tickers_analysis


def view_selected_page(scope):
	
	page = scope.page_to_display
	# print( 'Rendering > ', page)
	
	page_map = {
						'home_page'			:view_project_welcome,
						'charts_primary'	:view_primary,
						'charts_secondary'	:view_secondary,
						'user'				:view_user,
						'single'			:single_ticker_analysis,
						'intraday'			:intraday_analysis,
						'volume'			:volume_analysis,
						'research'			:research_analysis,
						'multi'				:multi_tickers_analysis,
						'scope'				:view_scope,
					}

	if page in list(page_map.keys()):
		page_map[page](scope)
	# else:
	# 	st.warning( ('No Page yet selected > ' + page) )



# Helper - stores the selected page from the sidebar so we stay where we are on re-renders
def store_page(page:str):
	st.session_state.page_to_display = page


