
import streamlit as st


def scope_dropdown(scope, label_name, list_options, index_pos=0):
	
	label_name = 'Select a :blue['+label_name.upper() +']'

	scope_dropdown = st.selectbox(
		label=label_name,
		options=list_options,
		index=index_pos,
		# placeholder=label_name,
		# label_visibility='hidden',
		)
	
	return scope_dropdown

