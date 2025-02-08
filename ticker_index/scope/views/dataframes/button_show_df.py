import logging
import streamlit as st


def button_show_ticker_index(scope):
	logging.debug("button_show_ticker_index")
	widget_key = 'widget_show_ticker_index'
	
	button = st.button(
						label='🗂 Ticker Index', 
						use_container_width=True, 
						type='secondary',
						key=widget_key,
						on_click=clicked_show_ticker_index_status,
						args=(scope,)
						)
	
	return button


def clicked_show_ticker_index_status(scope):
	logging.warning("clicked_show_ticker_index_status")
	previous_value = scope.ticker_index['show']['ticker_index']
	new_value = True if previous_value == False else False
	scope.ticker_index['show']['ticker_index'] = new_value

	if new_value == True:
		scope.ticker_index['show']['industry_report'] = False
		scope.ticker_index['show']['editable_df'] = False
