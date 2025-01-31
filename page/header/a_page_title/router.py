import logging
import streamlit as st
from page.header.a_page_title.heading import add_page_title 
from page.header.a_page_title.buttons.download import button_download_ticker
from page.header.a_page_title.buttons.trials import button_show_trial_settings
from page.header.a_page_title.buttons.strategies import button_show_strategy_config
from page.header.a_page_title.buttons.charts import button_show_chart_settings
from page.header.a_page_title.buttons.overlays import button_show_overlay_settings
from page.header.a_page_title.dropdown_config import dropdown_select_config
from page.header.a_page_title.buttons.reset_page import button_reset_page


def build_page_header_title_row(scope):
	logging.debug("build_page_header_title_row")
	page = scope.display['page']

	col1,col2,col3,col4,col5,col6 = st.columns([7.0,2.0,0.5,0.5,1.0,1.0])  #12
	match page:
		case 'welcome':
			(scope)
		case 'logout':
			add_page_title(scope)
		case 'screener':
			with col1:add_page_title(scope)
			with col2:button_download_ticker(scope)
			with col3:button_show_trial_settings(scope)
			with col4:button_show_strategy_config(scope)		# TODO - replace with Settings when built
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case 'chart':
			with col1:add_page_title(scope)
			with col2:button_download_ticker(scope)
			with col3:button_show_chart_settings(scope)
			with col4:button_show_overlay_settings(scope)
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case 'intraday':
			with col1:add_page_title(scope)
			with col2:button_download_ticker(scope)
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case 'volume':
			with col1:add_page_title(scope)
			with col2:button_download_ticker(scope)
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case 'research':
			with col1:add_page_title(scope)
			with col2:button_download_ticker(scope)
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case 'websites':
			with col1:add_page_title(scope)
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case 'ticker_index':
			with col1:add_page_title(scope)
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case 'scope':
			with col1:add_page_title(scope)
			with col6:button_reset_page(scope)
		case 'testing':
			with col1:add_page_title(scope)
			with col5:dropdown_select_config(scope)
			with col6:button_reset_page(scope)
		case _:st.write(":red[Unknown Page Called = "+page+"]")
					
		

		


