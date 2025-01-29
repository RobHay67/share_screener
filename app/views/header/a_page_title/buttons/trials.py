import streamlit as st


def button_show_trial_settings(scope):

	page = scope.config['display']
	current_value = scope.page[page]['show']['trials']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='🧪', 
						use_container_width=True, 
						on_click=trial_config_status, args=(scope, ),
						type=type_of_button,
						help='Trial Settings'
						)

	return button

def trial_config_status(scope):

	page = scope.config['display']

	previous_value = scope.page[page]['show']['trials']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['trials'] = new_value









