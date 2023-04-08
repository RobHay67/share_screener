
import streamlit as st

def app_config_button(scope):

	page = scope.display_page
	current_value = scope.pages[page]['render']['app_config']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '⚙️', 
					use_container_width=True, 
					on_click=app_config_status, args=(scope, ),
					type=type_of_button,
					help='Page Configuration'
					)

	return button



def app_config_status(scope):

	page = scope.display_page

	previous_value = scope.pages[page]['render']['app_config']
	new_value = True if previous_value == False else False

	scope.pages[page]['render']['app_config'] = new_value