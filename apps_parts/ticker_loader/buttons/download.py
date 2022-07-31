import streamlit as st


def download_button(scope):

	download_button_msg = 'Download most recent ' + str(int(scope.data['download']['days'])) + ' day'
	download_button_msg = 'Download ' + str(int(scope.data['download']['days'])) + ' most recent day'
	if scope.data['download']['days'] > 1: download_button_msg += 's'

	return st.button(download_button_msg)

	