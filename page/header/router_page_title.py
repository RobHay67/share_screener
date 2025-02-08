import logging
import streamlit as st
from page.header.a_title.heading import page_name_and_icon 
from page.header.a_title.buttons.download import button_download_ticker
from page.header.a_title.buttons.trials import button_show_trial_settings
from page.header.a_title.buttons.strategies import button_show_strategy_config
from page.header.a_title.buttons.charts import button_show_chart_settings
from page.header.a_title.buttons.overlays import button_show_overlay_settings
from page.header.a_title.buttons.active_trial_or_chart import button_show_active_trials_or_charts
from page.header.a_title.dropdown_config import dropdown_select_config
from page.header.a_title.buttons.reset_page import button_reset_page


def page_title(scope):
	logging.info("page_title")
	page = scope.display['page']

	col1,col2,col3,col4,col5,col6,col7 = st.columns([6.5,2.0,0.5,0.5,0.5,1.0,1.0])  #12
	match page:
		case 'welcome':
			page_name_and_icon(scope)
		case 'logout':
			page_name_and_icon(scope)
		case 'screener':
			with col1:page_name_and_icon(scope)
			with col2:button_download_ticker(scope)
			with col3:button_show_trial_settings(scope)
			with col4:button_show_strategy_config(scope)
			with col5:button_show_active_trials_or_charts(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case 'chart':
			with col1:page_name_and_icon(scope)
			with col2:button_download_ticker(scope)
			with col3:button_show_chart_settings(scope)
			with col4:button_show_overlay_settings(scope)
			with col5:button_show_active_trials_or_charts(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case 'intraday':
			with col1:page_name_and_icon(scope)
			with col2:button_download_ticker(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case 'volume':
			with col1:page_name_and_icon(scope)
			with col2:button_download_ticker(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case 'research':
			with col1:page_name_and_icon(scope)
			with col2:button_download_ticker(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case 'websites':
			with col1:page_name_and_icon(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case 'ticker_index':
			with col1:page_name_and_icon(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case 'scope':
			with col1:page_name_and_icon(scope)
		case 'testing':
			with col1:page_name_and_icon(scope)
			with col6:dropdown_select_config(scope)
			with col7:button_reset_page(scope)
		case _:st.write(":red[Unknown Page Called = "+page+"]")
					
		

		


