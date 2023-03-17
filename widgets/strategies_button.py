import streamlit as st

def strategies_button(scope):

	app = scope.apps['display_app']
	current_value = scope.apps[app]['render']['strategy']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='Strategies', 
						use_container_width=True, 
						on_click=strategy_status, args=(scope, ),
						type=type_of_button
						)

	return button

def strategy_status(scope):
	app = scope.apps['display_app']

	previous_value = scope.apps[app]['render']['strategy']
	new_value = True if previous_value == False else False

	scope.apps[app]['render']['strategy'] = new_value


