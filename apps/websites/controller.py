import streamlit as st

from partials.app_header.controller import render_app_header



def render_websites(scope):

	render_app_header(scope, 'Internet Resources')

	col1,col2 = st.columns([4,4])


	with col1:
		st.write('Kitco News')
		st.write('Upcomming Dividends')
		st.write('Director Transactions')
		st.write('Global Indicies')
		st.write('Trading Economics')
		st.write('Finfiz - Ticker Map (proportional)')
		# st.write('Yahoo Finance')
		st.write('Investing.com')
		st.write('Yield Curve')
		# st.write('Google Finance')
		# st.write('ASX Company Data')
		st.write('')
		st.write('')
		st.write('')


	with col2:
		st.write('https://www.kitco.com')

		st.write('https://www.marketindex.com.au/upcoming-dividends')

		st.write('https://www.marketindex.com.au/director-transactions')
		st.write('https://markets.businessinsider.com/indices')
		st.write('https://tradingeconomics.com/commodities')
		st.write('https://finviz.com/map.ashx?t=sec_all&st=w52')
		# st.write('https://au.finance.yahoo.com/')
		st.write('https://au.investing.com')
		st.write('https://stockcharts.com/freecharts/yieldcurve.php')
		# st.write('https://www.google.com/finance/')
		# st.write('https://www2.asx.com.au/markets/company/cba')
		st.write('')
		st.write('')
		st.write('')
		st.write('')





