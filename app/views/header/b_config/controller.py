import streamlit as st

from app.views.header.b_config.page_config import show_specific_page_config
from app.views.header.b_config.trial_verdicts import show_trial_verdicts
from config.views.chart_config import show_chart_config

from charts.views.settings.controller_charts import show_chart_settings
from charts.views.settings.controller_overlays import show_overlay_config

from screener.views.settings.controller_trials import show_trial_settings
from screener.views.settings.controller_strategy import show_strategy_config


# I am expecting that this just points to config which is stored in other
# places around the code base
# ie chart config is stored in the Chart module





def show_page_config(scope):

	# Show or hide the appropriate Configuration Section
	page = scope.pages['display']

	if scope.pages[page]['render']['app_config'] == True:
		show_specific_page_config(scope)
		if page == 'screener':
			show_trial_verdicts(scope)
		if page == 'chart':
			show_chart_config(scope)

	# Chart Page Only
	if scope.pages[page]['render']['chart_settings'] == True:
		show_chart_settings(scope)

	if scope.pages[page]['render']['overlay_settings'] == True:
		show_overlay_config(scope)

	# Screener Page Only
	if scope.pages[page]['render']['trial_settings'] == True:
		show_trial_settings(scope)

	if scope.pages[page]['render']['strategy'] == True:
		show_strategy_config(scope)