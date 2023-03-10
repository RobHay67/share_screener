import streamlit as st

from partials.reports.dfs import render_ticker_dfs
from partials.reports.dfs import render_chart_dfs
from partials.reports.dfs import render_trial_dfs


def render_optional_information(scope):
    
	app = scope.apps['display_app']

	# Render optional information
	if scope.apps[app]['render']['tickers'] == True:
		render_ticker_dfs(scope)
	if scope.apps[app]['render']['charts'] == True:
		render_chart_dfs(scope)
	if scope.apps[app]['render']['trials'] == True:
		render_trial_dfs(scope)

