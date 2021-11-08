
import streamlit as st

from ticker_index import render_ticker_index_page
from ticker_data import render_ticker_data_files, render_ticker_list

from analysis_company import render_company_profile_page
from analysis_intraday import render_intraday_analysis_page
from analysis_multi import render_analysis_multi_page
from analysis_single import render_single_analysis_page
from analysis_volume import render_volume_page
from scope import render_scope_page

from ticker_data import load_ticker_data_files, load_and_download_ticker_data

def set_page(page:str):
	st.session_state.display_page = page

def render_welcome(scope):
	st.title(scope.project_description)
	st.success('Loaded and Ready for Analysis')

def render_current_page(page):
	print( 'Rendering > ', page)
	page_render_map = {
						'initial_load'		:render_welcome,

						'ticker_index'		:render_ticker_index_page,
						'ticker_list'		:render_ticker_list,
						'share_data_files'	:render_ticker_data_files,

						'analysis_multi'	:render_analysis_multi_page,
						'single_analysis'	:render_single_analysis_page,
						'company_profile'	:render_company_profile_page,
						'volume'			:render_volume_page,
						'intraday_analysis'	:render_intraday_analysis_page,

						'scope'				:render_scope_page,

					}

	if page in list(page_render_map.keys()):
		page_render_map[page](st.session_state)
	else:
		st.warning( ('No Page yet selected > ' + page) )





