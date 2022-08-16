import streamlit as st


def download_industry_message(scope, message):
	with scope.col5:
		st.write(  message )