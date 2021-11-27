import streamlit as st


def download_button(scope):

	download_button_msg = 'Download most recent ' + str(int(scope.download_days)) + ' day'
	download_button_msg = 'Download ' + str(int(scope.download_days)) + ' most recent day'
	if scope.download_days > 1: download_button_msg += 's'

	return st.button(download_button_msg)

	