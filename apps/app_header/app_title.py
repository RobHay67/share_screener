import streamlit as st

from widgets.app_config import app_config_button
from widgets.chart_config import chart_config_button
from widgets.chart_config import chart_overlay_button
from widgets.strategies_button import strategies_button
from widgets.trial_config import trial_config_button

def render_app_title(scope, title):
    
	app = scope.apps['display_app']

	# Render Page Title
	col1,col2,col3,col4 = st.columns([10.5,0.5,0.5,0.5])
	with col1:
		st.subheader(title)
	if app == 'chart':
		with col2:chart_overlay_button(scope)
		with col3:chart_config_button(scope)
	if app == 'screener':
		with col2:strategies_button(scope)
		with col3:trial_config_button(scope)
	with col4:
		app_config_button(scope)
		


