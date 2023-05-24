
import streamlit as st

def page_config_button(scope):

	page = scope.pages['display']
	current_value = scope.pages[page]['render']['app_config']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '⚙️', 
					use_container_width=True, 
					on_click=page_config_status, args=(scope, ),
					type=type_of_button,
					help='Page Configuration'
					)

	return button



def page_config_status(scope):

	page = scope.pages['display']

	previous_value = scope.pages[page]['render']['app_config']
	new_value = True if previous_value == False else False

	scope.pages[page]['render']['app_config'] = new_value