import logging
import streamlit as st

from charts.scope.views.settings_charts import show_settings_charts
from charts.scope.views.settings_overlay import show_settings_overlay
from trials.scope.view.settings_trials import show_settings_trials
from trials.scope.view.config_strategy import show_config_strategy

# Show/Hide additional config information or settings as specified by the user

def router_show_settings(scope):
	logging.debug("router_show_settings")
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

	