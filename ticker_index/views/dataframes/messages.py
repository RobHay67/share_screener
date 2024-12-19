import streamlit as st





def message_missing_ticker_file(scope):
	st.toast(
		'Ticker Index File does not exist at path > ' 
		+ str(scope.files['paths']['ticker_index']), 
		icon='⚠️'
		)

def messgae_creation_success():
	st.toast(
		'Successfully created empty Ticker Index Dataframe / File', 
		icon='🏆'
		)
	
def message_saved_ticker_index_file():
	st.toast(
		'Saved the Ticker Index File', 
		icon='💾'
		)
	
def message_records_added(number_of_new_records):

	if number_of_new_records > 0:
		st.toast(
			'Added '
			+ str(number_of_new_records) 
			+ ' to ticker index', 
			icon = '⚠️'
			)
	else:
		st.toast(
			'Zero Records added to ticker index', 
			icon = 'ℹ️'
			)



	