import streamlit as st
from app.views.header.f_worklists.dropdown_worklist import worklist_dropdown
from app.views.header.f_worklists.dropdown_errors import ticker_load_and_download_errors_dropdown
from app.views.header.f_worklists.dropdown_active_tests import active_chart_or_test_dropdown


def show_worklist_dropdowns(scope):
	page=scope.pages['display']
	if page in ['screener', 'chart', 'intraday', 'volume', 'research']:
		col1,col2,col3 = st.columns([7.0, 3.0, 2.0])  #12
		with col1:worklist_dropdown(scope)
		with col2:ticker_load_and_download_errors_dropdown(scope)
		with col3:active_chart_or_test_dropdown(scope)
		st.divider()
    




