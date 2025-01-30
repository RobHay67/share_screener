import streamlit as st
import pytz
from datetime import datetime

from markets.schema import opening_hours
from page.sidebar.row_limit import edit_row_limit
from page.sidebar.download import edit_download_days

def show_sidebar_app_info(scope):

	local_time=datetime.now()
	market_timezone = opening_hours[scope.config['share_market']]['timezone']
	market_time = datetime.now(pytz.timezone(market_timezone))

	st.logo('assets/Logo JPG.jpg')
	
	with st.sidebar:
		st.write('Welcome      : ' +  scope.users['login_name'])
		st.write('Share Market : ' + str(scope.config['share_market']))
		# st.write('Market Date  : ' + str(local_time.strftime('%Y-%m-%d')))
		st.write('Market Date  : ' + str(local_time.strftime('%a-%d-%b')))
		st.write('Market Time  : ' + str(market_time.strftime('%H:%M:%S %p')))
		st.caption('Local Time : ' + str(local_time.strftime('%H:%M:%S %p')))

		edit_download_days(scope)
	
		edit_row_limit(scope)






