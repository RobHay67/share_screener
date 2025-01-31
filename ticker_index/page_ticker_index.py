import logging
import streamlit as st

from page.header.controller import add_page_header
from ticker_index.scope.views.industries.report import render_industry_report
from ticker_index.scope.views.industries.button import button_industry_report
from ticker_index.scope.views.dataframes.button_show_df import button_show_ticker_index
from ticker_index.scope.views.dataframes.button_edit_df import button_edit_ticker_index_df
from ticker_index.scope.views.dataframes.editable_df import render_editable_ticker_index_df
from ticker_index.scope.views.dataframes.ticker_index import render_ticker_index_df
from ticker_index.scope.views.download.download_button import button_download_ticker_index


# Page Configuration
scope = st.session_state
scope.display['page'] = 'ticker_index'
logging.info("page = ticker_index")

add_page_header(scope)

if scope.users['logged_in']:
	col1,col2 = st.columns([10,2]) #12
	
	with col1:
		no_of_tickers_in_index = str((len(scope.ticker_index['df'])))
		st.write('Currently ' + no_of_tickers_in_index + ' codes in the ticker index')
	with col2:
		st.caption("< scope.ticker_index['df'] >")

	col1,col2,col3,col4 = st.columns([3,3,3,3]) #12
	with col1:button_show_ticker_index(scope)
	with col2:button_edit_ticker_index_df(scope)
	with col3:button_industry_report(scope)
	with col4:button_download_ticker_index(scope)
				
	render_industry_report(scope)
	render_editable_ticker_index_df(scope)
	render_ticker_index_df(scope)
		

	# TODO Yfinance messages





