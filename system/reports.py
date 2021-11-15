
import streamlit as st




def view_3_columns( description, variable, variable_name, diff_col_size=None ):
	if diff_col_size == None:
		col1,col2,col3 = st.columns([2,4,2])
	else:
		col1,col2,col3 = st.columns(diff_col_size)
	
	with col1: st.write(description)
	with col2: st.write(variable)
	with col3: st.write( ('< ' + variable_name + ' >') )







# def view_2_columns( description, variable ):
# 	col1,col2,col3 = st.columns([2,4,2])
	
# 	with col1: st.write(description)
# 	with col2: st.write(variable)