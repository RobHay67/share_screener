import logging
import streamlit as st
from config.scope.buttons.button_choose_scope import scope_button
from config.scope.buttons.button_data_type import data_type_button
from config.scope.buttons.show_config_value import show_config_single_value, show_config_values
from config.scope.buttons.dropdown_choose_scope import scope_dropdown


def show_config_config(scope):
	logging.info("show_config_config")
	scope_button(scope, "Config (App)", scope.config, make_red=True, suffix_only=False)
	scope_button(scope, "scope.config", scope.config, make_red=False, suffix_only=False)
	
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1.5,1.5,1,1,1,1,1,1])
	with col1:scope_button(scope, "scope.config['project_description']", scope.config['project_description'])
	with col2:scope_button(scope, "scope.config['project_start_time']", scope.config['project_start_time'])
	with col3:scope_button(scope, "scope.config['page_list']", scope.config['page_list'])
	with col4:scope_button(scope, "scope.config['ticker_search']", scope.config['ticker_search'])
	with col5:scope_button(scope, "scope.config['row_limit']", scope.config['row_limit'])
	with col6:scope_button(scope, "scope.config['share_market']", scope.config['share_market'])
	with col7:scope_button(scope, "scope.config['download_days']", scope.config['download_days'])
	with col8:scope_button(scope, "scope.config['external_link']", scope.config['external_link'])
	
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1.5,1.5,1,1,1,1,1,1])
	with col1:show_config_single_value("project_description", scope.config['project_description'])
	with col2:show_config_single_value("project_start_time", scope.config['project_start_time'])
	with col5:show_config_single_value("row_limit", scope.config['row_limit'])
	with col6:show_config_single_value("share_market", scope.config['share_market'])
	with col7:show_config_single_value("download_days", scope.config['download_days'])
	with col8:show_config_single_value("external_link", scope.config['external_link'])

	col1,col2 = st.columns([5,3])
	with col1:scope_button(scope, "Schemas", 'Click on the Schema Buttons', make_red=False, suffix_only=False)
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
	with col1:scope_button(scope, "scope.config['page_schema']", scope.config['page_schema'])
	with col2:scope_button(scope, "scope.config['external_links']", scope.config['external_links'])
	with col3:scope_button(scope, "scope.config['markets']", scope.config['markets'])
	with col4:scope_button(scope, "scope.config['public_holidays']", scope.config['public_holidays'])
	with col5:scope_button(scope, "scope.config['opening_hours']", scope.config['opening_hours'])

	col1,col2 = st.columns([3,6])
	with col2:scope_button(scope, "scope.config['dropdowns']", scope.config['dropdowns'], make_red=False, suffix_only=False)
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col4:scope_button(scope, "scope.config['dropdowns']['markets']", scope.config['dropdowns']['markets'])
	with col5:scope_button(scope, "scope.config['dropdowns']['industries']", scope.config['dropdowns']['industries'])
	with col6:scope_button(scope, "scope.config['dropdowns']['tickers']", scope.config['dropdowns']['tickers'])
	with col7:scope_button(scope, "scope.config['dropdowns']['ticker']", scope.config['dropdowns']['ticker'])
	with col8:scope_button(scope, "scope.config['dropdowns']['ohlcv_columns']", scope.config['dropdowns']['ohlcv_columns'])
	with col9:scope_button(scope, "scope.config['dropdowns']['price_columns']", scope.config['dropdowns']['price_columns'])
	
	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)
