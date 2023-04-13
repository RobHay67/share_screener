import streamlit as st


from pages.widgets.active import edit_active

def render_activate_metric(scope, config_key):
	edit_active(scope, 'charts', config_key)


