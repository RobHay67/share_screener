import streamlit as st
from widgets.worklist import render_worklist
from widgets.worklist import render_ticker_load_and_download_errors


def ticker_worklist_layer(scope):

	col1,col2,col3 = st.columns([6.5, 4.0, 1.5])  #12

	with col1:render_worklist(scope)
	with col2:render_ticker_load_and_download_errors(scope)

    




