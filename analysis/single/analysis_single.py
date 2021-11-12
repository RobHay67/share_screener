
import streamlit as st



# from web_components import render_data_loader, render_ticker_data_file

from web.data_loader import render_data_loader
from web.ticker_file import render_ticker_file


# ==============================================================================================================================================================
# Single Ticker Analysis Render Controller
# ==============================================================================================================================================================


def render_single_analysis_page(scope):
	st.header('Analysis - Single Ticker')

	render_data_loader(scope, 'single')

	# render_ticker_data_file(scope, ticker)