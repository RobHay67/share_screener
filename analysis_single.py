
import streamlit as st



from web_components import render_data_loader, render_ticker_data_file


# ==============================================================================================================================================================
# Single Ticker Analysis Render Controller
# ==============================================================================================================================================================


def render_single_analysis_page(scope):
	st.header('Analysis - Single Ticker')

	render_data_loader(scope, 'single')

	# render_ticker_data_file(scope, ticker)