import streamlit as st

from app.scope.views.config_pages import show_scope_page
from tickers.scope.view.config_ticker_schema import show_ticker_page_config

from charts.scope.views.settings.settings_chart import show_settings_chart
from charts.scope.views.settings.settings_overlay import show_settings_overlay
from screener.scope.view.settings.settings_trials import show_settings_trials

from screener.scope.view.config_trials import show_scope_trials
from screener.scope.view.config_trials import show_trial_verdicts
from screener.scope.view.config_strategy import show_scope_strategy
from charts.scope.views.config_chart import show_scope_chart

# Show/Hide additional config information or settings as specified by the user

def show_page_config_and_settings(scope):
	page = scope.config['display']

	if scope.page[page]['render']['page_config'] == True:
		show_scope_page(scope)
	
	if scope.page[page]['render']['ticker_config'] == True:
		show_ticker_page_config(scope)

	if page == 'screener':
		if scope.page[page]['render']['trial_settings'] == True:
			show_settings_trials(scope)
		if scope.page[page]['render']['strategy'] == True:
			show_scope_strategy(scope)
		if scope.page[page]['render']['page_config'] == True:
			st.divider()
			st.subheader('Screener Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_scope_trials(scope)
			show_trial_verdicts(scope)
			show_scope_strategy(scope)
		
	if page == 'chart':
		if scope.page[page]['render']['chart_settings'] == True:
			show_settings_chart(scope)
		if scope.page[page]['render']['overlay_settings'] == True:
			show_settings_overlay(scope)
		if scope.page[page]['render']['page_config'] == True:
			st.divider()
			st.subheader('Charts Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_scope_chart(scope)

	