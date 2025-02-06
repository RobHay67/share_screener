import logging
import streamlit as st
from page.header.d_worklists.dropdown_worklist import dropdown_worklist
from page.header.d_worklists.dropdown_errors import dropdown_load_and_download_ticker_errors
from page.header.d_worklists.dropdown_active_tests import dropdown_active_charts_or_trials


def row_page_list_dropdowns(scope):
	logging.info("row_page_list_dropdowns")
	page=scope.display['page']
	if page in ['screener', 'chart', 'intraday', 'volume', 'research']:
		col1,col2,col3 = st.columns([7.0, 3.0, 2.0])  #12
		with col1:dropdown_worklist(scope)
		with col2:dropdown_load_and_download_ticker_errors(scope)
		with col3:dropdown_active_charts_or_trials(scope)
    




