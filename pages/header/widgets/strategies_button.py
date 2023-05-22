import streamlit as st

def strategies_button(scope):

	page = scope.pages['display']
	current_value = scope.pages[page]['render']['strategy']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='♟️', 
						use_container_width=True, 
						on_click=strategy_status, args=(scope, ),
						type=type_of_button,
						help='Strategies - save current tests into a strategy'
						)

	return button

def strategy_status(scope):
	page = scope.pages['display']

	previous_value = scope.pages[page]['render']['strategy']
	new_value = True if previous_value == False else False

	scope.pages[page]['render']['strategy'] = new_value


