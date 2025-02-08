import logging
import streamlit as st


def button_show_overlay_settings(scope):
	logging.info("button_show_overlay_settings")
	page = scope.display['page']
	current_value = scope.page[page]['show']['overlays']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '📈', 
					use_container_width=True, 
					on_click=clicked_show_overlay_settings, args=(scope, page, ),
					type=type_of_button,
					help='Overlays - lines to put over the top of various charts'
					)
	return 

def clicked_show_overlay_settings(scope, page):
	logging.warning("clicked_show_overlay_settings")
	previous_value = scope.page[page]['show']['overlays']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['overlays'] = new_value