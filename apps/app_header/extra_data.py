import streamlit as st


from apps.app_header.page_config import render_page_config
from apps.reports.dfs import render_loaded_df
from apps.reports.dfs import render_df_with_added_cols

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
		render_strategies(scope)



def render_dataframes(scope):
	
	app = scope.apps['display_app']
	if scope.apps[app]['render']['ticker_file'] != 'Show/Hide Data':
		render_loaded_df(scope)

	if scope.apps[app]['render']['col_added_df'] != 'Show/Hide Data':
		render_df_with_added_cols(scope)



