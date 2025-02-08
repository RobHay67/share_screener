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
						on_click=clicked_save_ticker_index,
						args=(scope,)
						)
	
	return button


def clicked_save_ticker_index(scope):
	logging.warning("clicked_save_ticker_index")
	scope.ticker_index['save_edited_df'] = True



