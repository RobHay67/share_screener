import streamlit as st

from app.views.header.a_page_title.buttons.config import page_config_button
from app.views.header.a_page_title.buttons.charts import chart_settings_button
from app.views.header.a_page_title.buttons.overlays import chart_overlay_button
from app.views.header.a_page_title.buttons.strategies import strategies_button
from app.views.header.a_page_title.buttons.trials import trial_settings_button
from app.views.header.a_page_title.buttons.dfs import ticker_config_button
from app.views.header.a_page_title.buttons.reset_page import reset_page_button
from app.views.header.a_page_title.buttons.download import download_button


def page_title_layer(scope, page_title, page_icon):
    
	page = scope.config['display']

	if page in ['streamlit_app', 'config', 'ticker_index', 'logout']:
		# Single Line Titles only
		st.subheader(page_icon + ' ' + page_title, divider='gray')
	else:
		col1,col2,col3,col4,col5,col6,col7 = st.columns([7.0,2.0,0.5,0.5,0.5,0.5,1.0])
		# All Other Pages
		with col1:st.subheader(page_icon + ' ' + page_title, divider='gray')
		if page in ['screener', 'chart', 'intraday', 'volume']:
			with col2:download_button(scope)
		if page == 'chart':
			with col3:chart_settings_button(scope)
			with col4:chart_overlay_button(scope)
		if page == 'screener':
			with col3:trial_settings_button(scope)
			with col4:strategies_button(scope)
		with col5:ticker_config_button(scope)
		with col6:page_config_button(scope)
		with col7:reset_page_button(scope)
		
		
			
	
		


