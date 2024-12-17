import streamlit as st


def button_save_ticker_index(scope):

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
	scope.ticker_index['render']['save_edited_df'] = True



