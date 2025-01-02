import streamlit as st

from app.views.header.b_config.page_config import show_specific_page_config
from config.views.chart_config import show_chart_config

from charts.views.settings.controller_charts import show_chart_settings
from charts.views.settings.controller_overlays import show_overlay_config

from screener.views.settings.user_trials import show_user_trial_settings
from screener.views.settings.user_strategy import show_strategy_config


# I am expecting that this just points to config which is stored in other
# places around the code base
# ie chart config is stored in the Chart module

# Show default page config
# then any extra config for specific pages



def show_page_config(scope):

	# Show or hide the appropriate Configuration Section
	page = scope.pages['display']

	if scope.pages[page]['render']['page_config'] == True:
		show_specific_page_config(scope)
		if page == 'screener':
			# show the extra trials general config
			# verdicts - we need something for this
			# show_trial_verdicts(scope)

			if scope.pages[page]['render']['trial_settings'] == True:
				show_user_trial_settings(scope)
			if scope.pages[page]['render']['strategy'] == True:
				show_strategy_config(scope)

		if page == 'chart':
			show_chart_config(scope)

			if scope.pages[page]['render']['chart_settings'] == True:
				show_chart_settings(scope)
			if scope.pages[page]['render']['overlay_settings'] == True:
				show_overlay_config(scope)

	