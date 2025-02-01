import logging
import streamlit as st
from ticker_index.scope.model.save import save_changes_into_ticker_index
from ticker_index.scope.views.dataframes.button_save_edits import button_save_ticker_index
from ticker_index.scope.views.dataframes.button_cancel_edit import button_cancel_index_changes

# Dropdowns are automatically used for categorical columns.



def render_editable_ticker_index_df(scope):
	logging.debug("render_editable_ticker_index_df")
	if scope.ticker_index['show']['editable_df']:
		
		widget_key = 'widget_' + 'edit_ticker_index_' + str(scope.ticker_index['editable_df_key'])
		uneditable_cols = scope.ticker_index['lists']['uneditable_columns']
		
		col1,col2,col3 = st.columns([6,3,3]) #12
		with col1:
			st.subheader('Editable Ticker Index Dataframe')
		with col2:
			button_save_ticker_index(scope)
		with col3:
			button_cancel_index_changes(scope)

	
		edited_df = st.data_editor(
			scope.ticker_index['df'],
			key = widget_key,
			disabled=uneditable_cols
			)

		if scope.ticker_index['save_edited_df']:
			save_changes_into_ticker_index(scope, edited_df)



