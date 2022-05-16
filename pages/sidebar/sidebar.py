import streamlit as st

from widgets.row_limit import edit_row_limit
from widgets.download_days import edit_download_days
from widgets.logout import logout_button


def render_sidebar(scope):
	
	st.sidebar.title(scope.config['project_description'])


	# if scope.users['login_name'] != 'Login to Use the Application':
	with st.sidebar:
		st.write('Welcome : ' +  scope.users['login_name'])


		st.subheader('Analysis')
		st.button('Single'  			, on_click=set_page, args=(scope, 'single', ))
		st.button('Intra-Day'			, on_click=set_page, args=(scope, 'intraday', ))
		st.button('Volume'				, on_click=set_page, args=(scope, 'volume', ))
		st.button('Research'			, on_click=set_page, args=(scope, 'research', ))
		st.button('Screener'			, on_click=set_page, args=(scope, 'screener', ))

		st.subheader('Chart Settings')
		st.button('Primary Charts'  	, on_click=set_page, args=(scope, 'charts_primary', ))
		st.button('Secondary Charts'	, on_click=set_page, args=(scope, 'charts_secondary', ))
		# st.button('Defaults'			, on_click=set_page, args=(scope, 'user', ))

		st.subheader('Download and Analysis Settings')
	
		edit_download_days(scope)
		edit_row_limit(scope)

		st.button('Config (scope)'		, on_click=set_page, args=(scope, 'scope', ))

		logout_button(scope)



def set_page(scope:dict, page:str):
	scope.pages['display_page'] = page




