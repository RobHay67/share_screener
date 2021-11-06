
import streamlit as st


# from share_data import load_tickers
from ticker_index import render_ticker_index_page
from share_data import render_share_data_page, render_share_data_file, render_ticker_list
from analysis_company import render_company_profile_page
from analysis_daily import render_daily_analysis_page
from analysis_volume import render_volume_page
from scope import render_scope_page
from multi_analysis import render_multi_analysis_page



def set_page(page:str):
	st.session_state.display_page = page

def render_current_page(page):

	page_render_map = {
						'ticker_index'		:render_ticker_index_page,
						'ticker_list'		:render_ticker_list,
						'manage_share_data'	:render_share_data_page,
						'share_data_files'	:render_share_data_file,
						'volume'			:render_volume_page,
						'company_profile'	:render_company_profile_page,
						'daily_analysis'	:render_daily_analysis_page,
						'scope'				:render_scope_page,
						'multi_analysis'	:render_multi_analysis_page,

					}

	if page in list(page_render_map.keys()):
		page_render_map[page](st.session_state)
	else:
		st.warning( ('No Page yet selected > ' + page) )









	# if   st.session_state.display_page == 'home': render_home_page(st.session_state)
  
	# if st.session_state.display_page == 'ticker_index': render_ticker_index_page(st.session_state)
	# elif st.session_state.display_page == 'ticker_list': render_ticker_list(st.session_state)
	# elif st.session_state.display_page == 'manage_share_data': render_share_data_page(st.session_state)
	# elif st.session_state.display_page == 'share_data_files': render_share_data_file(st.session_state)
	# elif st.session_state.display_page == 'volume':	render_volume_page(st.session_state)  
	# elif st.session_state.display_page == 'company_profile': render_company_profile_page(st.session_state)
	# elif st.session_state.display_page == 'daily_analysis': render_daily_analysis_page(st.session_state)
	# elif st.session_state.display_page == 'scope': render_scope_page(st.session_state)

	# elif st.session_state.display_page == 'multi_analysis': st.info('Clicked on Multi Ticker Analysis')




