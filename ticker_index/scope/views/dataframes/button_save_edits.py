import logging
import streamlit as st


def button_save_ticker_index(scope):
	logging.debug("button_save_ticker_index")
	widget_key = 'widget_save_ticker_index'
	
	button = st.button(
						label='💾 Save Changes', 
						use_container_width=True, 
						type='secondary',
						key=widget_key,
						on_click=save_changes_to_ticker_index,
						args=(scope,)
						)
	
	return button


def save_changes_to_ticker_index(scope):
	logging.debug("save_changes_to_ticker_index")
	scope.ticker_index['save_edited_df'] = True



