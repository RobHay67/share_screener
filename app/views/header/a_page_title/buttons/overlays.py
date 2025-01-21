import streamlit as st


def button_show_overlay_settings(scope):

	page = scope.config['display']
	current_value = scope.page[page]['show']['settings_overlay']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '📈', 
					use_container_width=True, 
					on_click=overlay_config_status, args=(scope, page, ),
					type=type_of_button,
					help='Overlays - lines to put over the top of various charts'
					)
	return 

def overlay_config_status(scope, page):

	previous_value = scope.page[page]['show']['settings_overlay']
	new_value = True if previous_value == False else False

	scope.page[page]['show']['settings_overlay'] = new_value