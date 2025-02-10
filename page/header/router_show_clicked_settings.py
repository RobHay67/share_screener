import logging
import streamlit as st

from charts.scope.view_settings_charts import show_settings_charts
from charts.scope.view_settings_overlay import show_settings_overlay
from trials.scope.view_settings_trials import show_settings_trials
from trials.scope.view_config_strategy import show_config_strategy

# Show/Hide additional config information or settings as specified by the user

def router_show_clicked_settings(scope):
	logging.info("router_show_clicked_settings")
	page = scope.display['page']

	match page:
		case 'screener':
			if scope.page[page]['show']['trials']:
				show_settings_trials(scope)
			if scope.page[page]['show']['strategy']:
				show_config_strategy(scope)
				
		case 'chart':
			if scope.page[page]['show']['charts']:
				show_settings_charts(scope)
			if scope.page[page]['show']['overlays']:
				show_settings_overlay(scope)

	