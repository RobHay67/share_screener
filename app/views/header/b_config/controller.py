import streamlit as st

from app.config.views.pages import show_specific_page_config
from charts.views.settings.controller_charts import show_chart_settings
from charts.views.settings.controller_overlays import show_overlay_config
from screener.views.settings.user_trials import show_user_trial_settings
from screener.views.settings.user_strategy import show_strategy_config

from app.config.views.trials import show_trial_general_config
from app.config.views.trials import show_trial_user_settings
from app.config.views.trials import show_trial_verdicts
from screener.views.settings.user_strategy import show_strategy_config
from app.config.views.charts import show_chart_config
from app.config.views.charts import show_chart_user_settings


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
		if scope.pages[page]['render']['trial_settings'] == True:
			show_user_trial_settings(scope)
		if scope.pages[page]['render']['strategy'] == True:
			show_strategy_config(scope)
		if scope.pages[page]['render']['page_config'] == True:
			st.divider()
			st.subheader('Screener Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_trial_general_config(scope)
			show_trial_verdicts(scope)
			show_trial_user_settings(scope)
			show_strategy_config(scope)
		
	if page == 'chart':
		if scope.pages[page]['render']['chart_settings'] == True:
			show_chart_settings(scope)
		if scope.pages[page]['render']['overlay_settings'] == True:
			show_overlay_config(scope)
		if scope.pages[page]['render']['page_config'] == True:
			st.divider()
			st.subheader('Charts Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_chart_config(scope)
			show_chart_user_settings(scope)

	