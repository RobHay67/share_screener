import streamlit as st


def select_a_market(scope):

	previous_selection = scope.pages['multi']['market']

	selected_market = st.selectbox(
									label='Add a Market to Ticker List',
									options=scope.dropdown_markets, 
									index=scope.dropdown_markets.index(previous_selection), 
									help='Select an Entire Share Market for Analysis',
									key='1'
									)

	scope.pages['multi']['market'] = selected_market
