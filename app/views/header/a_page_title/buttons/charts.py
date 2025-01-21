import streamlit as st


def button_show_chart_settings(scope):

	page = scope.config['display']
	current_value = scope.page[page]['render']['chart_settings']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='📊', 
						use_container_width=True, 
						on_click=chart_settings_status, 
						args=(scope, page, ),
						type=type_of_button,
						help='Chart Configuration Settings'
						)
	return button

def chart_settings_status(scope, page):
	
	previous_value = scope.page[page]['render']['chart_settings']
	new_value = True if previous_value == False else False

	scope.page[page]['render']['chart_settings'] = new_value


