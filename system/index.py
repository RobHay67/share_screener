import streamlit as st

from index.load import load_ticker_index_file


def scope_index(scope):
	# Primary Application Objects
	scope.ticker_index = {}						# was previous ticker_index_file
	load_ticker_index_file(scope)
	

def render_index(scope):
	col1,col2 = st.columns([6,2])
	
	with col1: st.subheader('Ticker Index File')
	with col2: st.write('< ticker_index >')

	st.dataframe(scope.ticker_index, 2000, 1200)




