import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_display(scope):


	col1,col2 = st.columns([3,3])
	with col1:st.write(':blue[This config is specially for this Config Page]')
	with col1:scope_button(scope, "Config to Display", scope.display['config_page'], make_red=True, suffix_only=False)
	with col1:scope_button(scope, "scope.display['config_page']", scope.display['config_page'], make_red=False, suffix_only=False)
	# with col1:scope_button(scope, "display_scope", scope.display['display_scope'], make_red=False, suffix_only=False)

	col1,col2,col3,col4 = st.columns([1,1,1,3])
	with col1:scope_button(scope, "config_key", scope.display['config_key'])
	with col2:scope_button(scope, "config_value", scope.display['config_value'])
	with col3:scope_button(scope, "config_page", scope.display['config_page'])

	# col1,col2,col3,col4 = st.columns([1,1,1,3])
	with col3:show_config_single_value("display_config_group", scope.display['config_page'])

	if scope.display['config_key'] != None:
		st.caption('Creates a Circular Reference (special code called)')
		# show_config_values(scope)
		button_pressed = scope.display['config_key']
		button_pressed = button_pressed.removeprefix('widget>')
		st.subheader(':blue[' + button_pressed +']')

		st.write("scope.display['config_page']   = " + scope.display['config_page'])
		st.write("scope.display['config_key']    = " + button_pressed)
		st.write("scope.display['config_value']  = " +scope.display['config_value'])
	
	st.divider()