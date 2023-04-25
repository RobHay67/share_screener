import streamlit as st

from pages.config.pages import render_page_config
from pages.chart.settings.controller import render_available_charts
from pages.chart.settings.overlays import render_overlays_config
from pages.screener.settings.controller import render_available_trials
from pages.config.strategies import render_strategies

def render_config_and_settings(scope):

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



