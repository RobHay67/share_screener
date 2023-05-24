import streamlit as st
import pytz
from datetime import datetime

from markets.schema import opening_hours
from pages.sidebar.row_limit import edit_row_limit
from pages.sidebar.download import edit_download_days

def render_sidebar(scope):

	local_time=datetime.now()
	market_timezone = opening_hours[scope.pages['share_market']]['timezone']
	market_time = datetime.now(pytz.timezone(market_timezone))

	# print('local_time      = ', local_time)
	# print('market_timezone = ', market_timezone)
	# print('market_time     = ', market_time)
	
	with st.sidebar:
		# st.title(scope.config['project_description'])
		st.write('Welcome      : ' +  scope.users['login_name'])
		st.write('Share Market : ' + str(scope.pages['share_market']))
		# st.write('Market Date  : ' + str(local_time.strftime('%Y-%m-%d')))
		st.write('Market Date  : ' + str(local_time.strftime('%a-%d-%b')))
		st.write('Market Time  : ' + str(market_time.strftime('%H:%M:%S %p')))
		st.caption('Local Time : ' + str(local_time.strftime('%H:%M:%S %p')))

		edit_download_days(scope)
	
		edit_row_limit(scope)






