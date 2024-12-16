import streamlit as st




def download_button(scope):

	# page = scope.pages['display']

	download_button_msg = 'Download Previous ' + str(int(scope.pages['download_days'])) + ' day'

	if scope.pages['download_days'] > 1: 
		download_button_msg += 's'
		
	button = st.button(
		label=download_button_msg, 
		# help="Press to download the previous X days. If button disabled, select ticker(s)",
		use_container_width=True, 
		)

	return button

	


