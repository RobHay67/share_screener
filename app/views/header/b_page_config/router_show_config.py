import streamlit as st

from screener.scope.view.config_trials import show_config_verdicts
from screener.scope.view.config_trials import show_config_trials
from screener.scope.view.config_strategy import show_config_strategy
from charts.scope.views.config_charts import show_config_charts
from ticker_index.scope.views.config_ticker_index import show_config_ticker_index
from app.scope.views.config_pages import show_config_pages
from tickers.scope.view.config_tickers import show_config_tickers


def router_show_config(scope):
	page = scope.config['display']
	config_to_show = scope.page[page]['show']['config_to_show']

	if config_to_show == 'Configuration':
		if page == 'screener':
			show_config_verdicts(scope)
			show_config_trials(scope)
			show_config_strategy(scope)
		if page == 'charts':
			show_config_charts(scope)
		if page == 'ticker_index':
			show_config_ticker_index(scope)
	
	if config_to_show == 'Page Config':
		show_config_pages(scope)

	if config_to_show == 'Ticker Data':
		show_config_tickers(scope)
	

		
