import streamlit as st

from pages.header.controller import render_app_header
from pages.reports.industries import render_industry_report
from pages.widgets.industries import industry_report_button
from pages.widgets.ticker_index import download_ticker_index_button

from pages.widgets.ticker_index import ticker_index_editable_df
from pages.widgets.ticker_index import save_ticker_index_button
from pages.widgets.ticker_index import render_ticker_index_messages


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
	no_of_tickers_in_index = str((len(scope.ticker_index['df'])))
	with col1:st.write('Currently ' + no_of_tickers_in_index + ' codes in the ticker index')
	with col2:st.caption("< scope.ticker_index['df'] >")

	col1,col2,col3 = st.columns([4,4,4]) #12

	with col1:save_ticker_index_button(scope)
	with col2:industry_report_button(scope)
	with col3:download_ticker_index_button(scope)
		
	render_industry_report(scope)

	render_ticker_index_messages(scope)

	# TODO Yfinance messages


	ticker_index_editable_df(scope)		# This is a copy of the original dataframe
	# This is the original output for this page	
	# st.dataframe(ticker_index_df, 2000, 1200)



