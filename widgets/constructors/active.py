import streamlit as st


from widgets.active import edit_active
from widgets.active import edit_active


def render_activate_metric(scope, metric):
	edit_active(scope, 'charts', metric)

