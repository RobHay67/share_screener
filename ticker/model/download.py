import streamlit as st



def scope_download(scope):
	scope.download_days 			= 7
	scope.download_industries 		= []
	scope.download_yf_files			= {}
	scope.downloaded_loaded_list 	= []
	scope.downloaded_missing_list 	= []
	scope.downloaded_yf_anomolies 	= {}




def set_download_days():
	download_days = st.sidebar.number_input( 
											'Days to Download (recent)', 
											min_value=7, 
											key='88'
											)
	return download_days
