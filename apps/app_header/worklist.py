import streamlit as st
from widgets.worklist import render_worklist


def render_ticker_worklist(scope):

	col1,col2,col3 = st.columns([6.0, 4.0, 2.0])  #12

	with col1:render_worklist(scope)

	with col2:st.write('put the erros lists here??')
    

    




