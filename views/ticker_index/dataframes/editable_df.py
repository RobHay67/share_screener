import streamlit as st

from ticker_index.schema import uneditable_columns
from ticker_index.save import save_changes_into_ticker_index

from views.ticker_index.dataframes.save_button import button_save_ticker_index
from views.ticker_index.dataframes.cancel_button import button_cancel_index_changes

# Dropdowns are automatically used for categorical columns.



def render_editable_ticker_index_df(scope):
    
	if scope.ticker_index['render']['editable_df']:
		
		widget_key = 'widget_' + 'edit_ticker_index_' + str(scope.ticker_index['render']['editable_df_key'])
		uneditable_cols = uneditable_columns(scope)
		
		st.subheader('Editable Ticker Index Dataframe')
		
		col1,col2,col3,col4 = st.columns([4,4,4,4]) #12
		with col1:
			button_save_ticker_index(scope)
		with col2:
			button_cancel_index_changes(scope)
	
		edited_df = st.data_editor(
			scope.ticker_index['df'],
			key = widget_key,
			disabled=uneditable_cols
			)


		if scope.ticker_index['render']['save_edited_df']:
			save_changes_into_ticker_index(scope, edited_df)



