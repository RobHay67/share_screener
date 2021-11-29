import streamlit as st

from config.model.set_page import set_page
from config.model.set_analysis_limit import set_analysis_row_limit
from config.model.set_download_days import set_download_days



def render_sidebar(scope):
	
	st.sidebar.title(scope.project_description)

	st.sidebar.subheader('Analysis')
	st.sidebar.button('Single'  			, on_click=set_page, args=('single', ))
	st.sidebar.button('Intra-Day'			, on_click=set_page, args=('intraday', ))
	st.sidebar.button('Volume'				, on_click=set_page, args=('volume', ))
	st.sidebar.button('Research'			, on_click=set_page, args=('research', ))
	st.sidebar.button('Multiple'			, on_click=set_page, args=('multi', ))

	st.sidebar.subheader('Charts')
	st.sidebar.button('Primary Charts'  	, on_click=set_page, args=('charts_primary', ))
	st.sidebar.button('Secondary Charts'	, on_click=set_page, args=('charts_secondary', ))
	# st.sidebar.button('Defaults'			, on_click=set_page, args=('user', ))

	st.sidebar.subheader('System Settings')
	st.sidebar.button('Settings'			, on_click=set_page, args=('scope', ))
	scope.download_days 					= set_download_days()
	scope.analysis_row_limit 				= set_analysis_row_limit()







