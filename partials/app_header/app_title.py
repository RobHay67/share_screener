import streamlit as st

from widgets.chart_config import chart_config_button


def render_app_title(scope, title):
    
	app = scope.apps['display_app']

	# Render Page Title
	col1,col2 = st.columns([11,2])
	with col1:
		st.subheader(title)
	if app == 'chart':
		with col2:chart_config_button(scope)


