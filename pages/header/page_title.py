import streamlit as st

from pages.widgets.app_config import app_config_button
from pages.widgets.chart_config import chart_config_button
from pages.widgets.chart_config import chart_overlay_button
from pages.widgets.strategies_button import strategies_button
from pages.widgets.trial_config import trial_config_button
from pages.widgets.reset_page import reset_page_render

def page_title_layer(scope, page_title, page_icon):
    
	page = scope.display_page

	if page in ['home', 'config', 'ticker_index', 'logout']:
		# Single Line Titles only
		st.subheader(page_icon + ' ' + page_title)

	else:
		# All Other Pages
		col1,col2,col3,col4,col5 = st.columns([9.5,0.5,0.5,0.5,1.0])
		
		with col1:
			st.subheader(page_icon + ' ' + page_title)
		with col4:
			app_config_button(scope)
		with col5:
			reset_page_render(scope)

		# Additional Information for chart and screener
		if page == 'chart':
			with col2:chart_overlay_button(scope)
			with col3:chart_config_button(scope)
		if page == 'screener':
			with col2:strategies_button(scope)
			with col3:trial_config_button(scope)
	
		

