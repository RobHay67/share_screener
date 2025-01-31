import logging
import streamlit as st
from config.scope.views.buttons.button_choose_scope import scope_button
from config.scope.views.buttons.button_data_type import data_type_button
from config.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from config.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_display(scope):
	logging.debug("show_config_display")

	col1,col2 = st.columns([4,3])
	with col1:st.write(':blue[This section is specifically for this Config Page]')
	with col1:scope_button(scope, "Config to Display", scope.display['config_page'], make_red=True, suffix_only=False)
	with col1:scope_button(scope, "scope.display", scope.display['config_page'], make_red=False, suffix_only=False)
	# with col1:scope_button(scope, "display_scope", scope.display['display_scope'], make_red=False, suffix_only=False)

	col1,col2,col3,col4,col5 = st.columns([1,1,1,1,3])
	with col1:scope_button(scope, "page", scope.display['page'])
	with col2:scope_button(scope, "config_key", scope.display['config_key'])
	with col3:scope_button(scope, "config_value", scope.display['config_value'])
	with col4:scope_button(scope, "config_page", scope.display['config_page'])

	with col1:show_config_single_value("show_page", scope.display['page'])
	with col4:show_config_single_value("display_config_group", scope.display['config_page'])

	if scope.display['config_key'] != None:
		st.caption('Creates a Circular Reference (special code called)')
		# show_config_values(scope)
		button_pressed = scope.display['config_key']
		button_pressed = button_pressed.removeprefix('widget>')
		st.subheader(':blue[' + button_pressed +']')

		st.write("scope.display['config_page']   = " + scope.display['config_page'])
		st.write("scope.display['config_key']    = " + button_pressed)
		st.write("scope.display['config_value']  = " + str(scope.display['config_value']))
	
	st.divider()