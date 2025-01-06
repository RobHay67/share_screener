import streamlit as st

from app.scope.views.pages import show_specific_page_config
from tickers.scope.view.config import show_ticker_page_config

from charts.scope.views.settings.controller_charts import show_chart_settings
from charts.scope.views.settings.controller_overlays import show_overlay_config
from screener.views.settings.controller import show_user_trial_settings
from screener.views.settings.user_strategy import show_user_strategy_settings

from screener.scope.view.trial_config import show_trial_general_config
from screener.scope.view.trial_config import show_trial_user_settings
from screener.scope.view.trial_config import show_trial_verdicts
from screener.scope.view.strategy_config import show_strategy_config
from charts.scope.views.config import show_chart_config
from charts.scope.views.config import show_chart_user_settings

# Show/Hide additional config information or settings as specified by the user

def show_page_config(scope):
	page = scope.pages['display']

	if scope.pages[page]['render']['page_config'] == True:
		show_specific_page_config(scope)
	
	if scope.pages[page]['render']['ticker_config'] == True:
		show_ticker_page_config(scope)

	if page == 'screener':
		if scope.pages[page]['render']['trial_settings'] == True:
			show_user_trial_settings(scope)
		if scope.pages[page]['render']['strategy'] == True:
			show_strategy_config(scope)
		if scope.pages[page]['render']['strategy'] == True:
			show_user_strategy_settings(scope)
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

	