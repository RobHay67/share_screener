import streamlit as st

from pages.header.controller import render_app_header
from pages.reports.industries import render_industry_report
from pages.header.widgets.industries import button_industry_report
from pages.ticker_index.save import button_save_ticker_index
from pages.ticker_index.download import button_download_ticker_index
from pages.ticker_index.data import ticker_index_editable_df
from pages.ticker_index.data import render_editable_ticker_df

# Page Configuration
page = 'ticker_index'
page_title = 'Ticker Index File'
page_icon = '🗄️'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


render_app_header(scope, page_title, page_icon)
st.write('Rob - we need to find how we can have a dropdown categorical to change values in certain columns')


if scope.users['logged_in']:

	col1,col2 = st.columns([10,2]) #12
	
	with col1:
		no_of_tickers_in_index = str((len(scope.ticker_index['df'])))
		st.write('Currently ' + no_of_tickers_in_index + ' codes in the ticker index')
	with col2:
		st.caption("< scope.ticker_index['df'] >")


	col1,col2,col3 = st.columns([4,4,4]) #12

	with col1:
		button_save_ticker_index(scope)
	with col2:
		button_industry_report(scope)
	with col3:
		button_download_ticker_index(scope)
		
	render_industry_report(scope)


	# TODO Yfinance messages


	# render ticker index as a dataframe

	render_editable_ticker_df(scope)


	# ticker_index_editable_df(scope)		# This is a copy of the original dataframe
	# This is the original output for this page	
	# st.dataframe(ticker_index_df, 2000, 1200)



