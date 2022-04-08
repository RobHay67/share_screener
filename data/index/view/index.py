import streamlit as st


def view_index(scope):
	col1,col2 = st.columns([6,2])
	
	with col1: st.subheader('Ticker Index File')
	with col2: st.write('< ticker_index >')

	st.dataframe(scope.data['ticker_index'], 2000, 1200)
