import streamlit as st

def set_streamlit_page_config():
	
	# Set the Browser Tab Name for the App
	st.set_page_config( 
			page_title='DDT - Data Driven Trading', 
			page_icon='📊',
			layout="wide",								# Allow wide Screen to be taken advantage of
			)
	
	# Padding Between Controls
	padding = 1.0
	st.markdown(f""" <style>
		.reportview-container .main .block-container{{
			padding-top: {padding}rem;
			padding-right: {padding}rem;
			padding-left: {padding}rem;
			padding-bottom: {padding}rem;
		}} </style> """, unsafe_allow_html=True)

	