import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_config_value import show_config_single_value, show_config_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown


def show_config_verdicts(scope):
	ticker_list = scope.tickers.keys()
	page='screener' # Verdicts are not relevant for any of the other pages

	scope_button(scope, "Verdicts", scope.tickers, make_red=True, suffix_only=False)
	scope_button(scope, "scope.tickers['ticker']['page']['verdicts']", scope.tickers, suffix_only=False)
	ticker = scope_dropdown(scope, 'ticker', ticker_list)
	scope_button(scope, "['screener']", "'screener' > only the Screener Page is relevant", make_red=False, suffix_only=True)
	
	if len(ticker_list)>0:
		scope_button(scope, "scope.tickers["+ticker+"]["+page+"]['verdicts]", scope.tickers[ticker][page]['verdicts'])

		col1,col2,col3 = st.columns([1,1,1])
		with col1:scope_button(scope, "scope.tickers[ticker][page]['verdicts']['verdict']", scope.tickers[ticker][page]['verdicts']['verdict'])
		with col2:scope_button(scope, "scope.tickers[ticker][page]['verdicts']['replace_verdict']", scope.tickers[ticker][page]['verdicts']['replace_verdict'])
		with col3:scope_button(scope, "scope.tickers[ticker][page]['verdicts']['trials']", scope.tickers[ticker][page]['verdicts']['trials'])

		with col1:show_config_single_value("verdicts", scope.tickers[ticker][page]['verdicts']['verdict'])
		with col2:show_config_single_value("replace_verdict", scope.tickers[ticker][page]['verdicts']['replace_verdict'])
	else: # we dont have any tickers 
		scope_button(scope, "Detailed Config Not Available until tickers loaded", scope.tickers, make_red=True, suffix_only=False)
		col1,col2,col3 = st.columns([1,1,1])
		with col1:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['verdict']", scope.tickers)
		with col2:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['replace_verdict']", scope.tickers)
		with col3:scope_button(scope, "scope.tickers['ticker']['screener']['verdicts']['trials']", scope.tickers)

	st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_config_values(scope)

