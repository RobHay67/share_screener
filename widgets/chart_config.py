import streamlit as st


def chart_config_button(scope):
	return st.button('Chart Config', use_container_width=True, on_click=chart_config_status, args=(scope, ))

def chart_overlay_button(scope):
	return st.button('Overlays', use_container_width=True, on_click=overlay_config_status, args=(scope, ))



def chart_config_status(scope):

	previous_value = scope.apps['chart']['render']['chart']
	new_value = True if previous_value == False else False

	scope.apps['chart']['render']['chart'] = new_value

def overlay_config_status(scope):

	previous_value = scope.apps['chart']['render']['overlay']
	new_value = True if previous_value == False else False

	scope.apps['chart']['render']['overlay'] = new_value