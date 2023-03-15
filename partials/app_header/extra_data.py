import streamlit as st

from partials.reports.dfs import render_ticker_dfs
from partials.reports.dfs import render_chart_dfs
from partials.reports.dfs import render_trial_dfs
from apps.chart.config.primary import render_primary_charts_config
from apps.chart.config.overlays import render_overlays_config
from partials.app_header.config import render_app_config

def render_config(scope):

	app = scope.apps['display_app']

	print('Current App   = ', app)
	print('Config stutus = ', scope.apps[app]['render']['config'])

	if scope.apps[app]['render']['config'] == True:
		render_app_config(scope)

	
	if scope.apps[app]['render']['chart'] == True:
		render_primary_charts_config(scope)
		

	if scope.apps[app]['render']['overlay'] == True:
		render_overlays_config(scope)



def render_optional_information(scope):
    
	app = scope.apps['display_app']

	# Render optional information

	if scope.apps[app]['render']['tickers'] == True:
		render_ticker_dfs(scope)
	if scope.apps[app]['render']['charts'] == True:
		render_chart_dfs(scope)
	if scope.apps[app]['render']['trials'] == True:
		render_trial_dfs(scope)





