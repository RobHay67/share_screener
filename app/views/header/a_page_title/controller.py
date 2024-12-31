import streamlit as st

from app.views.header.a_page_title.page_config import page_config_button
from charts.views.settings.chart_settings import chart_settings_button
from charts.views.settings.chart_settings import chart_overlay_button
from app.views.header.a_page_title.strategies_button import strategies_button
from screener.views.trials.trial_settings import trial_settings_button
from app.views.header.a_page_title.reset_page import reset_page_render
from app.views.header.a_page_title.download_button import download_button

def page_title_layer(scope, page_title, page_icon):
    
	page = scope.pages['display']

	if page in ['streamlit_app', 'config', 'ticker_index', 'logout']:
		# Single Line Titles only
		st.subheader(page_icon + ' ' + page_title, divider='gray')
	else:
		# All Other Pages
		col1,col2,col3,col4,col5,col6 = st.columns([7.5,2.0,0.5,0.5,0.5,1.0])
		
		with col1:st.subheader(page_icon + ' ' + page_title, divider='gray')
		with col5:page_config_button(scope)
		with col6:reset_page_render(scope)
		
		# Download button for appropriate pages
		if page in ['screener', 'chart', 'intraday', 'volume']:
			with col2:download_button(scope)

		# Additional Information for chart and screener
		if page == 'chart':
			with col3:chart_settings_button(scope)
			with col4:chart_overlay_button(scope)
		if page == 'screener':
			with col3:trial_settings_button(scope)
			with col4:strategies_button(scope)
			
	
		


