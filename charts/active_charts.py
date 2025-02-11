import logging
import streamlit as st


def show_active_charts(scope):
	logging.info("show_active_charts")
	
	# Introduction
	col1,col2 = st.columns([4,8])
	with col1:st.subheader('Charts - active only')
	col1,col2,col3,col4,col5,col6,col7 = st.columns([2,1,1,1,7,1,1])
	
	# headings
	with col1:st.caption('Chart Name')
	with col2:st.caption('Short Name')
	with col3:st.caption('Overlay ?')
	with col4:st.caption('Add Overlay')
	with col5:st.caption('Notes')
	with col6:st.caption('Definition')
	with col7:st.caption('Config Ref')
	st.divider()

	for chart in scope.charts['active_list']:
		col1,col2,col3,col4,col5,col6,col7 = st.columns([2,1,1,1,7,1,1])

		definition = scope.charts['user_config'][chart]['definition']
		with col1: st.write(scope.charts['user_config'][chart]['name'])
		with col2: st.write(scope.charts['user_config'][chart]['short_name'])
		with col3: st.write(scope.charts['user_config'][chart]['is_overlay'])
		with col4: st.write(scope.charts['user_config'][chart]['add_overlays'])
		with col5: st.write(scope.charts['user_config'][chart]['notes'])
		with col6: st.write("[defintion]("+definition+")")
		with col7: st.write(chart)

