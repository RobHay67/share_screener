import streamlit as st



def set_download_days():
	download_days = st.sidebar.number_input( 
											'Days to Download (recent)', 
											min_value=7, 
											key='88'
											)
	return download_days


