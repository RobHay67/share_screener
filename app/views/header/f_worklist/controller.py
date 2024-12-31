import streamlit as st
from app.views.header.http_mark_down import http_mark_down_for_header
from app.views.header.f_worklist.dropdown import render_worklist_dropdown
from app.views.header.f_worklist.errors import render_ticker_load_and_download_errors
from app.views.header.f_worklist.active_tests import render_active_charts_or_tests


def render_ticker_worklist(scope):
	page=scope.pages['display']
	if page in ['screener', 'chart', 'intraday', 'volume', 'research']:
		col1,col2,col3 = st.columns([7.0, 3.0, 2.0])  #12
		with col1:render_worklist_dropdown(scope)
		with col2:render_ticker_load_and_download_errors(scope)
		with col3:render_active_charts_or_tests(scope)
    




