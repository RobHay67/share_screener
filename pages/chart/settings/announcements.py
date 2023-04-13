import streamlit as st


from pages.widgets.active import edit_active



def render_announcements(scope):
	config_key = 'announcements'
	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key)


