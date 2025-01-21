import streamlit as st

from app.scope.views.pages import show_scope_page
from tickers.scope.view.config import show_ticker_page_config

from charts.scope.views.settings.controller_charts import show_chart_settings
from charts.scope.views.settings.controller_overlays import show_overlay_config
from screener.scope.view.settings.controller import show_user_trial_settings

from screener.scope.view.trial_config import show_scope_trials
from screener.scope.view.trial_config import show_trial_verdicts
from screener.scope.view.strategy_config import show_strategy_config
from charts.scope.views.chart_config import show_scope_chart

# Show/Hide additional config information or settings as specified by the user

def show_page_config_and_settings(scope):
	page = scope.config['display']

	if scope.page[page]['render']['page_config'] == True:
		show_scope_page(scope)
	
	if scope.page[page]['render']['ticker_config'] == True:
		show_ticker_page_config(scope)

	if page == 'screener':
		if scope.page[page]['render']['trial_settings'] == True:
			show_user_trial_settings(scope)
		if scope.page[page]['render']['strategy'] == True:
			show_strategy_config(scope)
		if scope.page[page]['render']['page_config'] == True:
			st.divider()
			st.subheader('Screener Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_scope_trials(scope)
			show_trial_verdicts(scope)
			show_strategy_config(scope)
		
	if page == 'chart':
		if scope.page[page]['render']['chart_settings'] == True:
			show_chart_settings(scope)
		if scope.page[page]['render']['overlay_settings'] == True:
			show_overlay_config(scope)
		if scope.page[page]['render']['page_config'] == True:
			st.divider()
			st.subheader('Charts Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_scope_chart(scope)

	