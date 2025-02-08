import logging
import streamlit as st


def button_edit_ticker_index_df(scope):
	logging.debug("button_edit_ticker_index_df")
	widget_key = 'widget_' + 'ticker_index' + '_editable'

	button = st.button(
					label = '🖊 Edit Ticker Index', 
					use_container_width=True, 
					on_click=clicked_edit_ticker_index_df, 
					args=(scope, ),
	# 				help='Edit data in the Ticker Index Dataframe (permitted cols only)',
					key=widget_key,
					)
	return button

def clicked_edit_ticker_index_df(scope):
	logging.warning("clicked_edit_ticker_index_df")
	previous_value = scope.ticker_index['show']['editable_df']
	new_value = True if previous_value == False else False
	scope.ticker_index['show']['editable_df'] = new_value

	if new_value == True:
		scope.ticker_index['show']['industry_report'] = False
		scope.ticker_index['show']['ticker_index'] = False


