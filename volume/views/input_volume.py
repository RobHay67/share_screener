import streamlit as st



def view_input_volume():
	col1,col2 = st.columns([2,10])
	with col1: ticker_current_volume = st.number_input("Current Volume", value=0, format="%d")
	return ticker_current_volume



