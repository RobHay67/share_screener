
import streamlit as st

def button_show_ticker_config(scope):

	page = scope.config['display']
	current_value = scope.page[page]['show']['config_ticker_data']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '🗄', 
					use_container_width=True, 
					on_click=ticker_config_status, args=(scope, ),
					type=type_of_button,
					help='Ticker Data'
					)

	return button



def ticker_config_status(scope):

	page = scope.config['display']

	previous_value = scope.page[page]['show']['config_ticker_data']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['config_ticker_data'] = new_value