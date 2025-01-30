import streamlit as st
from config.scope.views.buttons.button_choose_scope import scope_button
from config.scope.views.buttons.button_data_type import data_type_button
from config.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from config.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_strategy(scope):

	scope_button(scope, "Strategies (WIP)", scope.strategy, make_red=True, suffix_only=False)
	scope_button(scope, "scope.strategy", scope.strategy, make_red=False, suffix_only=False)

	col1,col2,col3,col4,col5,col6,col7 = st.columns([1,1,1,1,1,2,2]) #9
	with col1:scope_button(scope, "scope.strategy['name']", scope.strategy['name'])
	with col2:scope_button(scope, "scope.strategy['price_columns']", scope.strategy['price_columns'])
	with col3:scope_button(scope, "scope.strategy['json_dict']", scope.strategy['json_dict'])
	with col4:scope_button(scope, "scope.strategy['results']", scope.strategy['results'])
	with col5:scope_button(scope, "scope.strategy['print_header']", scope.strategy['print_header'])
	with col6:scope_button(scope, "scope.strategy['header']", scope.strategy['header'])
	with col7:scope_button(scope, "scope.strategy['print']", scope.strategy['print'])

	col1,col2,col3,col4,col5 = st.columns([5,1,1,1,1])
	with col2:scope_button(scope, "scope.strategy['header']['build'] ", scope.strategy['header']['build'] )
	with col3:scope_button(scope, "scope.strategy['header']['rows']", scope.strategy['header']['rows'])
	with col4:scope_button(scope, "scope.strategy['print']['count']", scope.strategy['print']['count'])
	with col5:scope_button(scope, "scope.strategy['print']['line']", scope.strategy['print']['line'])

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)
