import streamlit as st


def scope_download(scope):
	# Download Ticker Variables
	# scope.download_days 			= 5  # now in user settings
	scope.download_industries 		= []
	scope.download_yf_files			= {}
	scope.downloaded_loaded_list 	= []
	scope.downloaded_missing_list 	= []
	scope.downloaded_yf_anomolies 	= {}


