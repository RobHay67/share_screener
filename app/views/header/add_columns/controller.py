# Add and Replace Dataframes and columns within Page Dataframes
# - refresh the page df (completely)
# - Refresh specific df columns (activate or change col_adders settings)
# - utilised the scope.tickers object to track what needs to be done

import streamlit as st

from app.views.header.format import md_for_header

from app.views.header.add_columns.progress_bar import render_progress_bar


def progress_adding_columns_to_data(scope):

	page = scope.pages['display']

	if page in ['chart','intraday','screener']:
		col1,col2,col3 = st.columns([1.5, 9.0, 1.5])  #12.0
		with col1:md_for_header('Add Columns to Ticker Files')
		with col2:render_progress_bar(scope, page)      # will add/update the columns as well!
























