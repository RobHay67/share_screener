import streamlit as st


from pages.widgets.active import edit_active



def render_announcements(scope):
	column_adder = 'announcements'
	type_config = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, type_config, column_adder)


