import streamlit as st


from pages.widgets.active import edit_active

def render_activate_metric(scope, column_adder):
	edit_active(scope, 'charts', column_adder)

