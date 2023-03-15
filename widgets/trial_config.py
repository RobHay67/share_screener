import streamlit as st


def trial_config_button(scope):
	return st.button('Trial Config', use_container_width=True, on_click=trial_config_status, args=(scope, ))

def trial_config_status(scope):

	app = scope.apps['display_app']

	previous_value = scope.apps[app]['render']['trial_config']
	new_value = True if previous_value == False else False

	scope.apps[app]['render']['trial_config'] = new_value
