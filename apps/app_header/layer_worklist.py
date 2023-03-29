import streamlit as st
from widgets.worklist import render_worklist_dropdown
from widgets.worklist import render_ticker_load_and_download_errors


def ticker_worklist_layer(scope):

	col1,col2,col3,col4 = st.columns([1.5, 6.5, 2.0, 2.0])  #12

	with col1:st.caption('Worklists')
	with col2:render_worklist_dropdown(scope)
	with col3:render_ticker_load_and_download_errors(scope)

    




