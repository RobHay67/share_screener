
import logging
import streamlit as st



def view_2_columns( description, variable ):
	logging.warning("view_2_columns")
	col1,col2,col3 = st.columns([2,2,8])
	with col1: st.write(description)
	with col2: st.write(variable)