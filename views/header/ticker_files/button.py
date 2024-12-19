import streamlit as st




def download_button(scope):

	download_button_msg = 'Download Interval = ' + str(scope.pages['download_days'])
		
	button = st.button(
		label=download_button_msg, 
		# help="Press to download the previous X days. If button disabled, select ticker(s)",
		use_container_width=True, 
		)

	return button

	


