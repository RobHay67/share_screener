import streamlit as st


def download_button(scope):

	# Note - this has been moved to the sidebar to imporove readibility of the limited screen realestate





	download_button_msg = 'Download most recent ' + str(int(scope.download['days'])) + ' day'
	download_button_msg = 'Download ' + str(int(scope.download['days'])) + ' most recent day'

	if scope.download['days'] > 1: 
		download_button_msg += 's'

	return st.button(download_button_msg)

	