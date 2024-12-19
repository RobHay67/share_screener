import streamlit as st

from views.config.pages import render_page_config
from views.chart.settings.controller import render_available_charts
from views.chart.settings.overlays import render_overlays_config
from views.screener.settings.controller import render_available_trials
from views.config.strategies import render_strategies

def render_config_buttons(scope):

	page = scope.pages['display']

	if scope.pages[page]['render']['app_config'] == True:
		render_page_config(scope)

	if scope.pages[page]['render']['chart_settings'] == True:
		render_available_charts(scope)

	if scope.pages[page]['render']['overlay_settings'] == True:
		render_overlays_config(scope)

	if scope.pages[page]['render']['trial_settings'] == True:
		render_available_trials(scope)

	if scope.pages[page]['render']['strategy'] == True:
		render_strategies(scope)



