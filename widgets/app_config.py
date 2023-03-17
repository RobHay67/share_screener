
import streamlit as st

def app_config_button(scope):

	app = scope.apps['display_app']
	current_value = scope.apps[app]['render']['app_config']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = 'App Config', 
					use_container_width=True, 
					on_click=app_config_status, args=(scope, ),
					type=type_of_button,
					)

	return button



def app_config_status(scope):

	app = scope.apps['display_app']

	previous_value = scope.apps[app]['render']['app_config']
	new_value = True if previous_value == False else False

	scope.apps[app]['render']['app_config'] = new_value