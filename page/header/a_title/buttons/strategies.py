import logging
import streamlit as st


def button_show_strategy_config(scope):
	logging.debug("button_show_strategy_config")
	logging.critical("Strategy Settings yet to be built")
	page = scope.display['page']
	current_value = scope.page[page]['show']['strategy']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='♟️', 
						use_container_width=True, 
						on_click=clicked_show_strategy, args=(scope, ),
						type=type_of_button,
						help='Strategy Settings'
						)

	return button

def clicked_show_strategy(scope):
	logging.warning("clicked_show_strategy")
	page = scope.display['page']

	previous_value = scope.page[page]['show']['strategy']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['strategy'] = new_value


