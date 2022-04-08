import streamlit as st

from pages.model.page import set_page
# from pages.model.data_status import redo_ohlc_data_all_pages_all_tickers
from pages.model.data_status import set_page_data_status




def on_change_row_limit(scope:dict):
	set_page_data_status(scope, shares=True, charts='all', tests='all' )




def render_sidebar(scope):
	
	st.sidebar.title(scope.config['project_description'])

	st.sidebar.subheader('Analysis')
	st.sidebar.button('Single'  			, on_click=set_page, args=('single', ))
	st.sidebar.button('Intra-Day'			, on_click=set_page, args=('intraday', ))
	st.sidebar.button('Volume'				, on_click=set_page, args=('volume', ))
	st.sidebar.button('Research'			, on_click=set_page, args=('research', ))
	st.sidebar.button('Screener'			, on_click=set_page, args=('screener', ))

	st.sidebar.subheader('Chart Settings')
	st.sidebar.button('Primary Charts'  	, on_click=set_page, args=('charts_primary', ))
	st.sidebar.button('Secondary Charts'	, on_click=set_page, args=('charts_secondary', ))
	# st.sidebar.button('Defaults'			, on_click=set_page, args=('user', ))

	

	st.sidebar.subheader('Download and Analysis Settings')

	scope.data['download']['days'] = 	st.sidebar.number_input( 
							'Days to Download (recent)', 
							min_value=7, 
							)

	scope.pages['row_limit'] =  st.sidebar.number_input( 
							'No of Rows for Analysis & Charts', 
							min_value=100, 
							on_change=on_change_row_limit,
							args=(scope, )
							)


	st.sidebar.button('Settings > all'		, on_click=set_page, args=('scope', ))







