
import streamlit as st


def three_cols( description, variable, variable_name, diff_col_size=None, widget_type='string' ):
	if diff_col_size == None:
		col1,col2,col3 = st.columns([2,2,2])
	else:
		col1,col2,col3 = st.columns(diff_col_size)
	
	with col1: 
		st.write(description)
	with col2: 
		if widget_type == 'string':
			st.write(variable)
		elif widget_type == 'selectbox':
			st.selectbox(label=variable_name, options=variable)
		elif  widget_type == 'multiselect':
			st.multiselect(label=variable_name, options=variable)
		elif  widget_type == 'df':
			st.dataframe(data=variable, width=None, height=None, use_container_width=True)
		else:
			st.write(variable)
		
	with col3: 
		st.write( ('< ' + variable_name + ' >') )





