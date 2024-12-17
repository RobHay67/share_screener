import streamlit as st

from views.header.controller import render_app_header
from views.ticker_index.industries.report import render_industry_report
from views.ticker_index.industries.button import button_industry_report
from views.ticker_index.dataframes.save_button import button_save_ticker_index
from views.ticker_index.download_button import button_download_ticker_index
from views.ticker_index.dataframes.edit_button import button_edit_ticker_index_df
from views.ticker_index.dataframes.editable_df import render_editable_ticker_index_df



# Page Configuration
page = 'ticker_index'
page_title = 'Ticker Index File'
page_icon = '🗄️'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


render_app_header(scope, page_title, page_icon)
st.write('Rob - we need to find how we can have a dropdown categorical to change values in certain columns')


if scope.users['logged_in']:

	col1,col2 = st.columns([10,2]) #12
	
	with col1:
		no_of_tickers_in_index = str((len(scope.ticker_index['df'])))
		st.write('Currently ' + no_of_tickers_in_index + ' codes in the ticker index')
	with col2:
		st.caption("< scope.ticker_index['df'] >")


	col1,col2,col3 = st.columns([4,4,4]) #12

	with col1:
		button_industry_report(scope)
		# button_save_ticker_index(scope)
	with col2:
		button_edit_ticker_index_df(scope)
	with col3:
		button_download_ticker_index(scope)
		
		
	render_industry_report(scope)
	render_editable_ticker_index_df(scope)
		

	# TODO Yfinance messages





