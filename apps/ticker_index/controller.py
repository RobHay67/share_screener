
import streamlit as st


from apps.reports.industries import render_industry_report
from widgets.industries import industry_report_button
from widgets.ticker_index import download_ticker_index_button

from widgets.ticker_index import ticker_index_editable_df
from widgets.ticker_index import save_ticker_index_button
from widgets.ticker_index import render_ticker_index_messages
from widgets.reset_page import reset_page_render


def render_ticker_index_page(scope):

	no_of_tickers_in_index = str((len(scope.ticker_index['df'])))

	col1,col2 = st.columns([10,2]) #12
	with col1:st.subheader('🗄️ Ticker Index File')
	with col1:st.write('Rob - we need to find how we can have a dropdown categorical to change values in certain columns')
	with col2:reset_page_render(scope)
	
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
