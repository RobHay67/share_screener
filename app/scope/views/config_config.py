import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_config(scope):

	scope_button(scope, "scope.config", scope.config, make_red=True, suffix_only=False)
	
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col1:scope_button(scope, "scope.config['project_description']", scope.config['project_description'])
	with col2:scope_button(scope, "scope.config['project_start_time']", scope.config['project_start_time'])
	with col3:scope_button(scope, "scope.config['page_schema']", scope.config['page_schema'])
	with col4:scope_button(scope, "scope.config['page_list']", scope.config['page_list'])
	with col5:scope_button(scope, "scope.config['ticker_search']", scope.config['ticker_search'])
	with col6:scope_button(scope, "scope.config['row_limit']", scope.config['row_limit'])
	with col7:scope_button(scope, "scope.config['display']", scope.config['display'])
	with col8:scope_button(scope, "scope.config['share_market']", scope.config['share_market'])
	with col9:scope_button(scope, "scope.config['download_days']", scope.config['download_days'])

	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col6:show_config_single_value("row_limit", scope.config['row_limit'])
	with col7:show_config_single_value("display", scope.config['display'])
	with col8:show_config_single_value("share_market", scope.config['share_market'])
	with col9:show_config_single_value("download_days", scope.config['download_days'])

	col1,col2 = st.columns([3,6])
	with col1:scope_button(scope, "scope.config['display_scope']", scope.config['display_scope'], make_red=False, suffix_only=False)
	with col2:scope_button(scope, "scope.config['dropdowns']", scope.config['dropdowns'], make_red=False, suffix_only=False)


	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col1:scope_button(scope, "scope.config['display_scope']['scope_key']", scope.config['display_scope']['scope_key'])
	with col2:scope_button(scope, "scope.config['display_scope']['scope_value']", scope.config['display_scope']['scope_value'])
	with col3:scope_button(scope, "scope.config['display_scope']['config_page']", scope.config['display_scope']['config_page'])
	with col4:scope_button(scope, "scope.config['dropdowns']['markets']", scope.config['dropdowns']['markets'])
	with col5:scope_button(scope, "scope.config['dropdowns']['industries']", scope.config['dropdowns']['industries'])
	with col6:scope_button(scope, "scope.config['dropdowns']['tickers']", scope.config['dropdowns']['tickers'])
	with col7:scope_button(scope, "scope.config['dropdowns']['ticker']", scope.config['dropdowns']['ticker'])
	with col8:scope_button(scope, "scope.config['dropdowns']['ohlcv_columns']", scope.config['dropdowns']['ohlcv_columns'])
	with col9:scope_button(scope, "scope.config['dropdowns']['price_columns']", scope.config['dropdowns']['price_columns'])

	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col3:show_config_single_value("display_config_group", scope.config['display_scope']['config_page'])
	
	
	st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_config_values(scope)
