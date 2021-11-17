
import streamlit as st


from home.view import view_project_welcome
from scope.view import view_scope
from scope.user.view import view_user
from charts.view import view_chart
from analysis.controller import single_ticker_page, intraday_page, volume_page, research_page, multi_tickers_page


def view_selected_page(page):
	# print( 'Rendering > ', page)
	page_view_map = {
						'home_page'		:view_project_welcome,
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






