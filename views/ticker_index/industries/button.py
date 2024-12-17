import streamlit as st



def button_industry_report(scope):

	widget_key = 'widget_' + 'ticker_index' + '_industry_report'

	button = st.button(
					label = '🏭 Tickers Grouped by Industry', 
					use_container_width=True, 
					on_click=change_industry_report_status, 
					args=(scope, ),
	# 				help='Show a Report by Industry (expandable to show codes)',
					key=widget_key,
					)

	return button

def change_industry_report_status(scope):

	previous_value = scope.ticker_index['render']['industry_report']
	new_value = True if previous_value == False else False

	scope.ticker_index['render']['industry_report'] = new_value


