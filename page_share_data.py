

import streamlit as st
from share_index import refresh_share_index_file


def render_share_data_page(streamlit_session):
	st.title('Load and/or Download Share Data')

	ticker_list_message = str(len(streamlit_session.ticker_list))
	# st.info(ticker_list_message)

	share_index_message = str((len(streamlit_session.share_index_file)))

	col1,col2,col3 = st.columns([3,3,3])
	with col1: st.subheader('Share Index File')
	with col1: st.write('No of Tickers in Share Index')
	with col1: st.success(share_index_message) 
	with col1: refresh_tickers = st.button('Update List of Valid Tickers')

	with col2: st.subheader('Load Share Data Files')
	with col2: st.write('Number of Tickers in the Ticker List')
	with col2: st.info(ticker_list_message) 
	with col2: load_tickers = st.button('Load OHLC Data')

	with col3: st.subheader('Download Share Data')
	with col3: st.write('Number of Tickers in the Ticker List')
	with col3: st.info(ticker_list_message) 
	with col3: download_tickers = st.button('Download OHLC Data')
	with col3: no_of_days = st.number_input('Number of Days to Download', min_value=1, max_value=10, value=1, key='0')    
	
	
	if refresh_tickers:
		refresh_share_index_file(st.session_state)

	if load_tickers:
		print( 'lets load the tickers in the ticker list')

	if download_tickers:
		print ( 'lets load what we have for these tickers and then download for the number of selected days')
	
	
	