import streamlit as st

from widgets.row_limit import edit_row_limit
from widgets.download_days import edit_download_days
from widgets.logout import logout_button

from tickers.download_controller import download_tickers
from partials.ticker_loader.buttons.download import download_button

import pytz
from datetime import datetime
from markets.schema import opening_hours

		

	


def render_sidebar(scope):
	
	st.sidebar.title(scope.config['project_description'])

	local_time=datetime.now()
	market_timezone = opening_hours[scope.config['share_market']]['timezone']
	market_time = datetime.now(pytz.timezone(market_timezone))
	
	if scope.users['login_name'] != 'Login to Use the Application':
		with st.sidebar:

			st.write('Welcome : ' +  scope.users['login_name'])
			st.write('Share Market : ' + str(scope.config['share_market']))
			st.write('Market Time : ' + str(local_time.strftime('%Y-%m-%d')) + '  ' + str(market_time.strftime('%H:%M:%S %p')))
			st.caption('Local Time : ' + str(local_time.strftime('%H:%M:%S %p')))

			edit_download_days(scope)
			download_new_ticker_data = download_button(scope)	
			if download_new_ticker_data: 
				download_tickers(scope)

			st.subheader('Analysis')
			st.button('Single'  			, on_click=set_page, args=(scope, 'single', ))
			st.button('IntraDay'			, on_click=set_page, args=(scope, 'intraday', ))
			st.button('Volume'				, on_click=set_page, args=(scope, 'volume', ))
			st.button('Research'			, on_click=set_page, args=(scope, 'research', ))
			st.button('Screener'			, on_click=set_page, args=(scope, 'screener', ))

			st.button('Websites'			, on_click=set_page, args=(scope, 'websites', ))

			st.subheader('Chart Settings')
			st.button('Primary Charts'  	, on_click=set_page, args=(scope, 'charts_primary', ))
			st.button('Secondary Charts'	, on_click=set_page, args=(scope, 'charts_secondary', ))

			# st.subheader('Download and Analysis Settings')
		
			# edit_download_days(scope)
			edit_row_limit(scope)

			st.button('Config (scope)'		, on_click=set_page, args=(scope, 'scope', ))
			
			st.write('---------')
			logout_button(scope)



def set_page(scope:dict, app:str):
	scope.apps['display_app'] = app




