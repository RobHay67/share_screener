
import streamlit as st

from index.web_page import render_index_page
from tickers.reports import render_ticker_data_files, render_ticker_list
from scope.render import scope_page


from analysis.web_pages import render_multi_page
# from analysis_single import render_single_analysis_page
from analysis.web_pages import render_single
from analysis.web_pages import render_intraday  
from analysis.web_pages import render_volume
# from analysis_volume import render_volume_page
from analysis.web_pages import render_research  


# from ticker_data import load_ticker_data_files, load_and_download_ticker_data
from tickers.file import load_ticker_data_files
from tickers.download import load_and_download_ticker_data


def set_page(page:str):
	st.session_state.display_page = page

def render_welcome(scope):
	st.title(scope.project_description)
	st.success('Loaded and Ready for Analysis')

def render_current_page(page):
	print( 'Rendering > ', page)
	page_render_map = {
						'initial_load'		:render_welcome,

						'ticker_index'		:render_index_page,
						'ticker_list'		:render_ticker_list,
						'share_data_files'	:render_ticker_data_files,
						'scope'				:scope_page,

						'analysis_multi'	:render_multi_page,
						'single_analysis'	:render_single,
						'intraday_analysis'	:render_intraday,
						'volume'			:render_volume,
						'research'			:render_research,

					}

	if page in list(page_render_map.keys()):
		page_render_map[page](st.session_state)
	else:
		st.warning( ('No Page yet selected > ' + page) )






