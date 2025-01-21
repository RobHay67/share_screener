import streamlit as st

from app.views.header.a_page_title.buttons.download import button_download_ticker
from app.views.header.a_page_title.buttons.charts import button_show_chart_settings
from app.views.header.a_page_title.buttons.overlays import button_show_overlay_settings
from app.views.header.a_page_title.buttons.trials import button_show_trial_settings
from app.views.header.a_page_title.buttons.strategies import button_show_strategy_config
from app.views.header.a_page_title.buttons.dfs import button_show_ticker_config
from app.views.header.a_page_title.buttons.page_config import button_show_page_config
from app.views.header.a_page_title.buttons.scope_config import button_show_app_scope
from app.views.header.a_page_title.buttons.reset_page import button_reset_page



def page_title_layer(scope, page_title, page_icon):
    
	page = scope.config['display']

	if page in ['streamlit_app', 'config', 'ticker_index', 'logout']:
		# Single Line Titles only
		st.subheader(page_icon + ' ' + page_title, divider='gray')
	else:
		col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([6.5,2.0,0.5,0.5,0.5,0.5,0.5,1.0])
		# All Other Pages
		with col1:st.subheader(page_icon + ' ' + page_title, divider='gray')
		if page in ['screener', 'chart', 'intraday', 'volume']:
			with col2:button_download_ticker(scope)
		if page == 'chart':
			with col3:button_show_chart_settings(scope)
			with col4:button_show_overlay_settings(scope)
		if page == 'screener':
			with col3:button_show_trial_settings(scope)
			with col4:button_show_strategy_config(scope)
		with col5:button_show_ticker_config(scope)
		with col6:button_show_page_config(scope)
		with col7:button_show_app_scope(scope)
		with col8:button_reset_page(scope)
		
		
			
	
		


