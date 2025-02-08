import logging
import streamlit as st


def button_show_chart_settings(scope):
	logging.debug("button_show_chart_settings")
	page = scope.display['page']
	current_value = scope.page[page]['show']['charts']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='📊', 
						use_container_width=True, 
						on_click=clicked_show_chart_settings, 
						args=(scope, page, ),
						type=type_of_button,
						help='Chart Configuration Settings'
						)
	return button

def clicked_show_chart_settings(scope, page):
	logging.warning("clicked_show_chart_settings")
	previous_value = scope.page[page]['show']['charts']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['charts'] = new_value


