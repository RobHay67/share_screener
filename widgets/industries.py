import streamlit as st



def select_industries(scope):

	selected_industries = st.multiselect(
									label='Add an Industry or Industries',
									options=scope.config['dropdowns']['industries'], 
									default=scope.pages['screener']['selectors']['industries'], 
									help='Quickly Select all tickers in a particular industry',
									key='2'
									)

	scope.pages['screener']['industries'] = selected_industries