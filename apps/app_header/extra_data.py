import streamlit as st


from apps.app_header.page_config import render_page_config
from apps.reports.dfs import render_ticker_dfs
from apps.reports.dfs import render_chart_dfs
from apps.reports.dfs import render_trial_dfs

from apps.chart.config.primary import render_primary_charts_config
from apps.chart.config.overlays import render_overlays_config
from apps.screener.config.controller import render_available_trials
from strategies.config import render_strategies




def render_config(scope):

	app = scope.apps['display_app']

	if scope.apps[app]['render']['app_config'] == True:
		render_page_config(scope)

	if scope.apps[app]['render']['chart_settings'] == True:
		render_primary_charts_config(scope)

	if scope.apps[app]['render']['overlay_settings'] == True:
		render_overlays_config(scope)

	if scope.apps[app]['render']['trial_settings'] == True:
		render_available_trials(scope)


	if scope.apps[app]['render']['strategy'] == True:
		print('Running render strategies')
		render_strategies(scope)



def render_optional_information(scope):
    
	app = scope.apps['display_app']

	if scope.apps[app]['render']['tickers'] == True:
		render_ticker_dfs(scope)
	if scope.apps[app]['render']['charts'] == True:
		render_chart_dfs(scope)
	if scope.apps[app]['render']['trials'] == True:
		render_trial_dfs(scope)




