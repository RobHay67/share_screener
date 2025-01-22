import streamlit as st

from charts.scope.views.settings_charts import show_settings_charts
from charts.scope.views.settings_overlay import show_settings_overlay
from screener.scope.view.settings_trials import show_settings_trials
from screener.scope.view.config_strategy import show_config_strategy

# Show/Hide additional config information or settings as specified by the user

def router_show_settings(scope):
	page = scope.config['display']

	match page:
		case 'screener':
			if scope.page[page]['show']['settings_trials']:
				show_settings_trials(scope)
			if scope.page[page]['show']['settings_strategy']:
				show_config_strategy(scope)
		case 'chart':
			if scope.page[page]['show']['settings_charts']:
				show_settings_charts(scope)
			if scope.page[page]['show']['settings_overlay']:
				show_settings_overlay(scope)

	