import streamlit as st


def trial_settings_button(scope):

	page = scope.display_page
	current_value = scope.pages[page]['render']['trial_settings']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='🧪', 
						use_container_width=True, 
						on_click=trial_config_status, args=(scope, ),
						type=type_of_button,
						help='Test Configuration Settings'
						)

	return button

def trial_config_status(scope):

	page = scope.display_page

	previous_value = scope.pages[page]['render']['trial_settings']
	new_value = True if previous_value == False else False

	scope.pages[page]['render']['trial_settings'] = new_value









