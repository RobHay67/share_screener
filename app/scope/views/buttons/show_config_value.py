import streamlit as st
from datetime import datetime 

# blue, green, orange, red, violet, gray/grey, rainbow.

def show_config_values(scope):
	button_pressed = scope.display['config_key']
	button_pressed = button_pressed.removeprefix('widget>')

	if button_pressed == "scope.config['project_start_time']":
		scope_value =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	else:
		scope_value = scope.display['config_value']
	
	st.subheader(':blue[' + button_pressed +']')
	st.write(scope_value)
	st.divider()


def show_config_single_value(label_name, scope_value):

	widget_key = 'widget>' + label_name
	if label_name == 'project_start_time':
		scope_value =  datetime.fromtimestamp(scope_value).strftime('%Y-%m-%d %H:%M:%S %p')
	if scope_value == True : scope_value = ":green["+str(scope_value)+"]"
	if scope_value == False : scope_value = ":red["+str(scope_value)+"]"
	if isinstance(scope_value, int): scope_value = ":blue["+str(scope_value)+"]"
	if isinstance(scope_value, str): scope_value = ":violet["+str(scope_value)+"]"

	button = st.button(
		label=str(scope_value), 
		key=widget_key, 
		use_container_width=True, 
		type='secondary',
		)
	return button