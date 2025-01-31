import logging
import streamlit as st
from config.scope.views.buttons.button_choose_scope import scope_button
from config.scope.views.buttons.button_data_type import data_type_button
from config.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from config.scope.views.buttons.dropdown_choose_scope import scope_dropdown





def show_config_files(scope):
	logging.debug("show_config_files")
	scope_button(scope, "Folders and Paths", scope.files, make_red=True, suffix_only=False)
	scope_button(scope, "scope.files", scope.files, make_red=False, suffix_only=False)

	col1,col2 = st.columns([5,4])
	with col1:scope_button(scope, "scope.files['folders']", scope.files['folders'], make_red=False, suffix_only=True)
	with col2:scope_button(scope, "scope.files['paths']", scope.files['paths'], make_red=False, suffix_only=True)
	
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)
	with col1:scope_button(scope, "scope.files['folders']['project']", scope.files['folders']['project'])
	with col2:scope_button(scope, "scope.files['folders']['files']", scope.files['folders']['files'])
	with col3:scope_button(scope, "scope.files['folders']['tickers']", scope.files['folders']['tickers'])
	with col4:scope_button(scope, "scope.files['folders']['results_analysis']", scope.files['folders']['results_analysis'])
	with col5:scope_button(scope, "scope.files['folders']['website']", scope.files['folders']['website'])
	with col6:scope_button(scope, "scope.files['paths']['users']", scope.files['paths']['users'])
	with col7:scope_button(scope, "scope.files['paths']['ticker_index']", scope.files['paths']['ticker_index'])
	with col8:scope_button(scope, "scope.files['paths']['website']", scope.files['paths']['website'])
	with col9:scope_button(scope, "scope.files['paths']['ticker_data']", scope.files['paths']['ticker_data'])

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)



