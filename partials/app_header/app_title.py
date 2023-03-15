import streamlit as st

from widgets.chart_config import chart_config_button
from widgets.chart_config import chart_overlay_button


def render_app_title(scope, title):
    
	app = scope.apps['display_app']

	# Render Page Title
	col1,col2,col3 = st.columns([9,2,2])
	with col1:
		st.subheader(title)
	if app == 'chart':
		with col2:chart_overlay_button(scope)
		with col3:chart_config_button(scope)
		


