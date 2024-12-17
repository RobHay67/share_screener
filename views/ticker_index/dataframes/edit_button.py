import streamlit as st


def button_edit_ticker_index_df(scope):

	widget_key = 'widget_' + 'ticker_index' + '_editable'

	button = st.button(
					label = '🖊 Edit Ticker Index', 
					use_container_width=True, 
					on_click=change_editable_df_status, 
					args=(scope, ),
	# 				help='Edit data in the Ticker Index Dataframe (permitted cols only)',
					key=widget_key,
					)

	return button

def change_editable_df_status(scope):
	previous_value = scope.ticker_index['render']['editable_df']
	new_value = True if previous_value == False else False
	scope.ticker_index['render']['editable_df'] = new_value


