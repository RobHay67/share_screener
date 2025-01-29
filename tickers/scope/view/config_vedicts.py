import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_verdicts(scope):
	col1,col2 = st.columns([3,3])
	ticker_list = scope.tickers.keys()
	page='screener' # Verdicts are not relevant for any of the other pages
	with col2:ticker = scope_dropdown(scope, 'Ticker', ticker_list)
	leader_text = "scope.tickers['"+ticker+"']['"+page+"']['verdicts']"
	with col2:scope_button(scope, "Verdicts ( "+ticker+" )", scope.tickers[ticker][page]['verdicts'], make_red=True, suffix_only=False)
	with col2:scope_button(scope, leader_text, scope.tickers[ticker][page]['verdicts'], suffix_only=False)
	
	if len(ticker_list)>0:
		with col2:scope_button(scope, leader_text+"['verdicts]", scope.tickers[ticker][page]['verdicts'])
		col1,col2,col3,col4 = st.columns([3,1,1,1])
		with col2:scope_button(scope, leader_text+"['verdict']", scope.tickers[ticker][page]['verdicts']['verdict'])
		with col3:scope_button(scope, leader_text+"['replace_verdict']", scope.tickers[ticker][page]['verdicts']['replace_verdict'])
		with col4:scope_button(scope, leader_text+"['trials']", scope.tickers[ticker][page]['verdicts']['trials'])

		with col2:show_config_single_value("verdicts", scope.tickers[ticker][page]['verdicts']['verdict'])
		with col3:show_config_single_value("replace_verdict", scope.tickers[ticker][page]['verdicts']['replace_verdict'])
	else: # we dont have any tickers 
		with col2:scope_button(scope, "Detailed Config Not Available until tickers loaded", scope.tickers, make_red=True, suffix_only=False)
		col1,col2,col3,col4 = st.columns([3,1,1,1])
		with col2:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['verdict']", scope.tickers)
		with col3:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['replace_verdict']", scope.tickers)
		with col4:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['trials']", scope.tickers)

	st.divider()
	if scope.display['config_key'] != None:
		show_config_values(scope)

