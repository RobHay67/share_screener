import streamlit as st
from datetime import datetime 


def show_scope_values(scope):
	button_pressed = scope.config['display_scope']['scope_key']
	button_pressed = button_pressed.removeprefix('widget>')

	if button_pressed == "scope.config['project_start_time']":
		scope_value =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	else:
		scope_value = scope.config['display_scope']['scope_value']
	
	st.subheader(':blue[' + button_pressed +']')
	st.write(scope_value)


def show_scope_single_value(label_name, scope_value):
	button = st.button(
		label=str(scope_value), 
		key=label_name, 
		use_container_width=True, 
		type='secondary',
		)
	return button