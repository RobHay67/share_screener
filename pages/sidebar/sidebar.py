import streamlit as st



from widgets.row_limit import render_row_limit
from widgets.download_days import render_download_days

def render_sidebar(scope):
	
	st.sidebar.title(scope.config['project_description'])

	st.sidebar.subheader('Analysis')
	st.sidebar.button('Single'  			, on_click=set_page, args=(scope, 'single', ))
	st.sidebar.button('Intra-Day'			, on_click=set_page, args=(scope, 'intraday', ))
	st.sidebar.button('Volume'				, on_click=set_page, args=(scope, 'volume', ))
	st.sidebar.button('Research'			, on_click=set_page, args=(scope, 'research', ))
	st.sidebar.button('Screener'			, on_click=set_page, args=(scope, 'screener', ))

	st.sidebar.subheader('Chart Settings')
	st.sidebar.button('Primary Charts'  	, on_click=set_page, args=(scope, 'charts_primary', ))
	st.sidebar.button('Secondary Charts'	, on_click=set_page, args=(scope, 'charts_secondary', ))
	# st.sidebar.button('Defaults'			, on_click=set_page, args=(scope, 'user', ))

	

	st.sidebar.subheader('Download and Analysis Settings')
	render_download_days(scope)
	render_row_limit(scope)


	st.sidebar.button('Settings > all'		, on_click=set_page, args=(scope, 'scope', ))




def set_page(scope:dict, page:str):
	scope.pages['display_page'] = page




