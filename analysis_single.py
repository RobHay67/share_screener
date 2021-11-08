
import streamlit as st



from ticker_loader import render_selectors_for_single_ticker


# ==============================================================================================================================================================
# Single Ticker Analysis Render Controller
# ==============================================================================================================================================================


def render_single_analysis_page(scope):
	st.header('Analysis - Single Ticker')

	render_selectors_for_single_ticker(scope, 'single')