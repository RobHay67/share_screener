
import streamlit as st
from datetime import datetime
from datetime import timedelta
import pytz

from config.markets.schema import opening_hours

def render_page_title(scope, title):

	col1,col2,col3,col4 = st.columns([6,2,2,1])
	
	local_time=datetime.now()
	market_timezone = opening_hours[scope.config['share_market']]['timezone']
	market_time = datetime.now(pytz.timezone(market_timezone))
	

	with col1:
		st.header(title)

	with col2:
		st.write('')
		st.caption('Local Time = ' + str(local_time.strftime('%H:%M:%S %p')))
		
	
	with col3:
		st.write('')
		st.write('Market Time = ' + str(market_time.strftime('%H:%M:%S %p')))


	with col4:
		st.write('')
		st.write(str(local_time.strftime('%Y-%m-%d')))
