import streamlit as st


def button_cancel_index_changes(scope):
	widget_key = 'widget_cancel_ticker_index_changes'
	
	button = st.button(
						label='🚫 Cancel Changes', 
						use_container_width=True, 
						type='secondary',
						key=widget_key,
						on_click=change_cancel_df_save_status,
						args=(scope,)
						)
	
	return button


def change_cancel_df_save_status(scope):
	# increment the key counter for the widget. This has the affect
	# of causing the object to be re-rendered to its initial postition
	# in effect 'resetting' the dataframe and cancelling any changes
	scope.ticker_index['editable_df_key'] += 1
