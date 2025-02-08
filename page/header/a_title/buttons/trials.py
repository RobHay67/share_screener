import logging
import streamlit as st


def button_show_trial_settings(scope):
	logging.debug("button_show_trial_settings")
	page = scope.display['page']
	current_value = scope.page[page]['show']['trials']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='🧪', 
						use_container_width=True, 
						on_click=clicked_show_trial_settings, args=(scope, ),
						type=type_of_button,
						help='Trial Settings'
						)

	return button

def clicked_show_trial_settings(scope):
	logging.warning("clicked_show_trial_settings")
	page = scope.display['page']

	previous_value = scope.page[page]['show']['trials']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['trials'] = new_value









