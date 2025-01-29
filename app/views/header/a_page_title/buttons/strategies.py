import streamlit as st

def button_show_strategy_config(scope):

	page = scope.config['display']
	current_value = scope.page[page]['show']['strategy']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='♟️', 
						use_container_width=True, 
						on_click=strategy_status, args=(scope, ),
						type=type_of_button,
						help='Strategy Settings'
						)

	return button

def strategy_status(scope):
	page = scope.config['display']

	previous_value = scope.page[page]['show']['strategy']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['strategy'] = new_value


