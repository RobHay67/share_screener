
import streamlit as st


def scope_dropdown(scope, list_options, index_pos=0):
	
	scope_dropdown = st.selectbox(
		label='Select from the Dropdown Menu',
		options=list_options,
		index=index_pos,
		)
	
	return scope_dropdown

