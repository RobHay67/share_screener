import streamlit as st


from config.model.set_active import edit_active





def render_activate_metric(scope, metric):
	edit_active(scope, 'charts', metric)


