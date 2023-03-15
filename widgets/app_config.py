
import streamlit as st

def app_config_button(scope):
	return st.button('App Config', use_container_width=True, on_click=app_config_status, args=(scope, ))



def app_config_status(scope):

	app = scope.apps['display_app']

	previous_value = scope.apps[app]['render']['app_config']
	new_value = True if previous_value == False else False

	scope.apps[app]['render']['app_config'] = new_value