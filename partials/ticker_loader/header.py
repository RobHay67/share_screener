
import streamlit as st

def render_page_title(scope, title):

	col1,col2 = st.columns([6,8])
	
	with col1:
		st.header(title)
