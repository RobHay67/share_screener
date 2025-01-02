
import streamlit as st

def ticker_config_button(scope):

	page = scope.pages['display']
	current_value = scope.pages[page]['render']['ticker_config']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '🗄', 
					use_container_width=True, 
					on_click=ticker_config_status, args=(scope, ),
					type=type_of_button,
					help='Ticker Configuration'
					)

	return button



def ticker_config_status(scope):

	page = scope.pages['display']

	previous_value = scope.pages[page]['render']['ticker_config']
	new_value = True if previous_value == False else False

	scope.pages[page]['render']['ticker_config'] = new_value