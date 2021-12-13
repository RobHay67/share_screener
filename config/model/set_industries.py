import streamlit as st



def select_industries(scope):

	selected_industries = st.multiselect(
									label='Add an Industry or Industries',
									options=scope.dropdown_industries, 
									default=scope.pages['screener']['industries'], 
									help='Quickly Select all tickers in a particular industry',
									key='2'
									)

	scope.pages['screener']['industries'] = selected_industries