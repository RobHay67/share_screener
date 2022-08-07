import streamlit as st


from widgets.active import edit_active


def render_activate_metric(scope, col_adder):
	edit_active(scope, 'charts', col_adder)


