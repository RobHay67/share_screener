import streamlit as st


def trial_config_button(scope):

	app = scope.apps['display_app']
	current_value = scope.apps[app]['render']['trial_config']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='Tests Config', 
						use_container_width=True, 
						on_click=trial_config_status, args=(scope, ),
						type=type_of_button,
						)

	return button

def trial_config_status(scope):

	app = scope.apps['display_app']

	previous_value = scope.apps[app]['render']['trial_config']
	new_value = True if previous_value == False else False

	scope.apps[app]['render']['trial_config'] = new_value
