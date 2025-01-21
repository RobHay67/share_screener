import streamlit as st

from app.scope.views.config_pages import show_scope_page

from tickers.scope.view.config_tickers import show_scope_tickers
from tickers.scope.view.config_ticker_schema import show_scope_tickers_schema


from charts.scope.views.settings.settings_charts import show_settings_chart
from charts.scope.views.settings.settings_overlay import show_settings_overlay
from screener.scope.view.settings.settings_trials import show_settings_trials

from screener.scope.view.config_trials import show_scope_trials
from screener.scope.view.config_trials import show_trial_verdicts
from screener.scope.view.config_strategy import show_scope_strategy
from charts.scope.views.config_chart import show_scope_chart

# Show/Hide additional config information or settings as specified by the user

def show_page_config_and_settings(scope):
	page = scope.config['display']

	if scope.page[page]['show']['config_page'] == True:
		show_scope_page(scope)
	
	if scope.page[page]['show']['config_ticker_data'] == True:
		show_scope_tickers(scope)
		# show_scope_tickers_schema(scope)

	if page == 'screener':
		if scope.page[page]['show']['settings_trials'] == True:
			show_settings_trials(scope)
		if scope.page[page]['show']['settings_strategy'] == True:
			show_scope_strategy(scope)
		if scope.page[page]['show']['config_page'] == True:
			st.divider()
			st.subheader('Screener Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_scope_trials(scope)
			show_trial_verdicts(scope)
			show_scope_strategy(scope)
		
	if page == 'chart':
		if scope.page[page]['show']['settings_charts'] == True:
			show_settings_chart(scope)
		if scope.page[page]['show']['settings_overlay'] == True:
			show_settings_overlay(scope)
		if scope.page[page]['show']['config_page'] == True:
			st.divider()
			st.subheader('Charts Page specific config')
			st.write('TODO we need to default dictionary obkect')
			show_scope_chart(scope)

	