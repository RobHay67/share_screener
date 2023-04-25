import streamlit as st
from pages.widgets.worklist import render_worklist_dropdown
from pages.widgets.worklist import render_ticker_load_and_download_errors
from pages.widgets.worklist import render_active_charts_or_tests

def ticker_worklist_layer(scope):

	page=scope.pages['display']

	if page in ['screener', 'chart', 'intraday', 'volume', 'research']:

		col1,col2,col3,col4 = st.columns([1.5, 6.5, 2.0, 2.0])  #12

		with col1:st.caption('Worklists')
		with col2:render_worklist_dropdown(scope)
		with col3:render_ticker_load_and_download_errors(scope)
		with col4:render_active_charts_or_tests(scope)
    




