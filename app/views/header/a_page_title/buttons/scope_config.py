import streamlit as st


def button_show_app_scope(scope):
	page = scope.config['display']
	current_value = scope.page[page]['render']['app_scope']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = '⚙️', 
					use_container_width=True, 
					on_click=status_app_scope, args=(scope, page, ),
					type=type_of_button,
					help='Scope (page)'
					)
	return button


def status_app_scope(scope, page):

	previous_value = scope.page[page]['render']['app_scope']
	new_value = True if previous_value == False else False

	scope.page[page]['render']['app_scope'] = new_value