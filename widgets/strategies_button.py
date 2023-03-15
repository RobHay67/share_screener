import streamlit as st

def strategies_button(scope):
	return st.button('Strategies', use_container_width=True, on_click=strategy_status, args=(scope, ))

def strategy_status(scope):
	app = scope.apps['display_app']

	previous_value = scope.apps[app]['render']['strategy']
	new_value = True if previous_value == False else False

	scope.apps[app]['render']['strategy'] = new_value


