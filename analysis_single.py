
import streamlit as st



from web_results import render_selectors_for_single_ticker




def render_single_analysis_page(scope):
	st.title('Analysis - Single Ticker')

	render_selectors_for_single_ticker(scope, 'ticker_for_single')