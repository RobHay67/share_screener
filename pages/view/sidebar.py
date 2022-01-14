import streamlit as st

from pages.model.set_page import set_page
from pages.model.set_page_rows_limit import set_page_row_limit
from tickers.model.set_download_days import set_download_days


def render_sidebar(scope):
	
	st.sidebar.title(scope.project_description)

	st.sidebar.subheader('Analysis')
	st.sidebar.button('Single'  			, on_click=set_page, args=('single', ))
	st.sidebar.button('Intra-Day'			, on_click=set_page, args=('intraday', ))
	st.sidebar.button('Volume'				, on_click=set_page, args=('volume', ))
	st.sidebar.button('Research'			, on_click=set_page, args=('research', ))
	st.sidebar.button('Screener'			, on_click=set_page, args=('screener', ))
	st.sidebar.button('Screener Metrics'	, on_click=set_page, args=('metrics', ), key='1')

	st.sidebar.subheader('Chart Settings')
	st.sidebar.button('Primary Charts'  	, on_click=set_page, args=('charts_primary', ))
	st.sidebar.button('Secondary Charts'	, on_click=set_page, args=('charts_secondary', ))
	# st.sidebar.button('Defaults'			, on_click=set_page, args=('user', ))

	# st.sidebar.subheader('Analysis')
	

	st.sidebar.subheader('Download and Analysis Settings')
	scope.download_days 					= set_download_days()
	scope.page_row_limit 					= set_page_row_limit()
	st.sidebar.button('Settings > all'		, on_click=set_page, args=('scope', ))







