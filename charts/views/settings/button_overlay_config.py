import streamlit as st


def chart_overlay_button(scope):

	page = scope.pages['display']
	current_value = scope.pages[page]['render']['overlay_settings']
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

	previous_value = scope.pages[page]['render']['overlay_settings']
	new_value = True if previous_value == False else False

	scope.pages[page]['render']['overlay_settings'] = new_value