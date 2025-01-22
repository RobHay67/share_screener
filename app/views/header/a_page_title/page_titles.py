import streamlit as st

from app.views.header.a_page_title.page_header import page_header 
from app.views.header.a_page_title.buttons.download import button_download_ticker
from app.views.header.a_page_title.buttons.charts import button_show_chart_settings
from app.views.header.a_page_title.buttons.overlays import button_show_overlay_settings
from app.views.header.a_page_title.buttons.trials import button_show_trial_settings
from app.views.header.a_page_title.buttons.strategies import button_show_strategy_config
from app.views.header.a_page_title.buttons.dfs import button_show_ticker_config
from app.views.header.a_page_title.buttons.page import button_show_page_config
from app.views.header.a_page_title.buttons.scope_config import button_show_app_scope
from app.views.header.a_page_title.buttons.reset_page import button_reset_page

from app.views.header.a_page_title.select_config import select_config_to_show

# Page			Title	Download	Settings_1	Setting_2	Ticker	Page	Config	Reset
#						Button								Data
# Screener 		x		x			Trials		Strategy	x		x		x		x	
# Charts		x		x			Charts		Overlays	x		x		wIP		x			there is an overlays button - see where this points	
# Intra Day		x		x									x		x		?		x			config not working
# Volume		x		x									x		x		x		x			config not working
# Research		x		x									fix		x		x		x			config not working	> Remove ticker data ?
# Website		x													x		x		x			config and remove ticker data and reset	
# Ticker Index	x															x		x			add buttons
# Scope			x													x		x		x			add buttons	
# Logout		x			
# Testing		x											x		x		x		x			leave ticker data for testing	


# TODO - update the calls from page_title_layer > these need to have the extra config removed as this is now stored in
# TODO scope.config['page_schema']
# TODO > same for function calls from show_page_header 


def page_title_layer(scope):
    
	page = scope.config['display']

	# col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([6.5,2.0,0.5,0.5,0.5,0.5,0.5,1.0]) #12
	col1,col2,col3,col4,col5,col6 = st.columns([6.5,2.0,0.5,0.5,1.5,1.0])  #12
	match page:
		case 'welcome':
			page_header(scope)
		case 'logout':
			page_header(scope)
		case 'screener':
			with col1:page_header(scope)
			with col2:button_download_ticker(scope)
			with col3:button_show_trial_settings(scope)
			with col4:button_show_strategy_config(scope)
			with col5:select_config_to_show(scope)
			with col6:button_reset_page(scope)
		case 'chart':
			with col1:page_header(scope)
			with col2:button_download_ticker(scope)
			with col3:button_show_chart_settings(scope)
			with col4:button_show_overlay_settings(scope)
			with col6:button_reset_page(scope)
		case 'intraday':
			with col1:page_header(scope)
			with col2:button_download_ticker(scope)
			with col5:button_show_ticker_config(scope)
			with col5:select_config_to_show(scope)
			with col6:button_reset_page(scope)
		case 'volume':
			with col1:page_header(scope)
			with col2:button_download_ticker(scope)
			with col5:select_config_to_show(scope)
			with col6:button_reset_page(scope)
		case 'research':
			with col1:page_header(scope)
			with col2:button_download_ticker(scope)
			with col5:select_config_to_show(scope)
			with col6:button_reset_page(scope)
		case 'websites':
			with col1:page_header(scope)
			with col5:select_config_to_show(scope)
			with col6:button_reset_page(scope)
		case 'ticker_index':
			with col1:page_header(scope)
			with col5:select_config_to_show(scope)
			with col6:button_reset_page(scope)
		case 'scope':
			with col1:page_header(scope)
			with col6:button_reset_page(scope)
		case 'testing':
			with col1:page_header(scope)
			with col5:select_config_to_show(scope)
			with col6:button_reset_page(scope)
		case _:st.write(":red[Unknown Page Called = "+page+"]")
					
		

		


