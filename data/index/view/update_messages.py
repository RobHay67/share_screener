import streamlit as st




def message_updating():

	st.info( 'Updating the records in the Ticker Index file ')




def message_warning(add_records_counter, message):

	if add_records_counter > 0:
		st.warning( message)
	else:
		st.info( message)


	# st.warning( message) if add_records_counter > 0 else st.info( message)