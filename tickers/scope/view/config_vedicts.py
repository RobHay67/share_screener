import logging
import streamlit as st
from config.scope.views.buttons.button_choose_scope import scope_button
from config.scope.views.buttons.button_data_type import data_type_button
from config.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from config.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_verdicts(scope):
	logging.debug("show_config_verdicts")
	col1,col2 = st.columns([3,3])
	ticker_list = scope.tickers.keys()
	page='screener' # Verdicts are not relevant for any of the other pages
	
	with col2:ticker = scope_dropdown(scope, 'Ticker', ticker_list)
		
	if len(ticker_list)>0:
		# we have tickers 
		leader_text = "scope.tickers['"+ticker+"']['"+page+"']['verdicts']"
		with col2:scope_button(scope, "Verdicts ( "+ticker+" )", scope.tickers[ticker][page]['verdicts'], make_red=True, suffix_only=False)
		with col2:scope_button(scope, leader_text, scope.tickers[ticker][page]['verdicts'], suffix_only=False)
		with col2:scope_button(scope, leader_text+"['verdicts]", scope.tickers[ticker][page]['verdicts'])
		col1,col2,col3,col4 = st.columns([3,1,1,1])
		with col2:scope_button(scope, leader_text+"['overall_verdict']", scope.tickers[ticker][page]['verdicts']['overall_verdict'])
		with col3:scope_button(scope, leader_text+"['re_run_trials']", scope.tickers[ticker][page]['verdicts']['re_run_trials'])
		with col4:scope_button(scope, leader_text+"['trial_verdicts']", scope.tickers[ticker][page]['verdicts']['trial_verdicts'])

		with col2:show_config_single_value("overall_verdict", scope.tickers[ticker][page]['verdicts']['overall_verdict'])
		with col3:show_config_single_value("re_run_trials", scope.tickers[ticker][page]['verdicts']['re_run_trials'])
	else: 
		# we dont have any tickers 
		with col2:scope_button(scope, "Detailed Config Not Available until tickers loaded", scope.tickers, make_red=True, suffix_only=False)
		col1,col2,col3,col4 = st.columns([3,1,1,1])
		with col2:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['overall_verdict']", scope.tickers)
		with col3:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['re_run_trials']", scope.tickers)
		with col4:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['trial_verdicts']", scope.tickers)

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)

