import streamlit as st


def chart_config_button(scope):

	app = scope.apps['display_app']
	current_value = scope.apps[app]['render']['chart_config']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
						label='Chart Config', 
						use_container_width=True, 
						on_click=chart_config_status, args=(scope, ),
						type=type_of_button
						)
	return button

def chart_config_status(scope):

	previous_value = scope.apps['chart']['render']['chart_config']
	new_value = True if previous_value == False else False

	scope.apps['chart']['render']['chart_config'] = new_value


def chart_overlay_button(scope):

	app = scope.apps['display_app']
	current_value = scope.apps[app]['render']['overlay_config']
	type_of_button = 'primary' if current_value == True else 'secondary'

	button = st.button(
					label = 'Overlays', 
					use_container_width=True, 
					on_click=overlay_config_status, args=(scope, ),
					type=type_of_button
					)
	return 

def overlay_config_status(scope):

	previous_value = scope.apps['chart']['render']['overlay_config']
	new_value = True if previous_value == False else False

	scope.apps['chart']['render']['overlay_config'] = new_value