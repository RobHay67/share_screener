import logging
import streamlit as st



def button_industry_report(scope):
	logging.debug("button_industry_report")
	widget_key = 'widget_' + 'ticker_index' + '_industry_report'

	button = st.button(
					label = '🏭 Tickers by Industry', 
					use_container_width=True, 
					on_click=change_industry_report_status, 
					args=(scope, ),
	# 				help='Show a Report by Industry (expandable to show codes)',
					key=widget_key,
					)

	return button

def change_industry_report_status(scope):
	logging.debug("change_industry_report_status")
	previous_value = scope.ticker_index['show']['industry_report']
	new_value = True if previous_value == False else False

	scope.ticker_index['show']['industry_report'] = new_value

	if new_value == True:
		scope.ticker_index['show']['ticker_index'] = False
		scope.ticker_index['show']['editable_df'] = False

