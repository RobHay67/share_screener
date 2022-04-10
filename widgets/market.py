import streamlit as st


def select_a_market(scope):

	previous_selection = scope.pages['screener']['selectors']['market']

	selected_market = st.selectbox(
									label='Add a Market to Ticker List',
									options=scope.config['dropdowns']['markets'], 
									index=scope.config['dropdowns']['markets'].index(previous_selection), 
									help='Select an Entire Share Market for Analysis',
									key='1'
									)

	scope.pages['screener']['market'] = selected_market