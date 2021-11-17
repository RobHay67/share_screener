
import streamlit as st


def three_cols( description, variable, variable_name, diff_col_size=None ):
	if diff_col_size == None:
		col1,col2,col3 = st.columns([2,4,2])
	else:
		col1,col2,col3 = st.columns(diff_col_size)
	
	with col1: st.write(description)
	with col2: st.write(variable)
	with col3: st.write( ('< ' + variable_name + ' >') )

