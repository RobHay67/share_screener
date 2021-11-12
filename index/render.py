
import streamlit as st


from index.download import new_tickers_from_web
from index.reports import industry_report



# ==============================================================================================================================================================
# Browser Render Controller : Display Ticker Index, Count of tickers by Industry and Update the Ticker Index
# ==============================================================================================================================================================

def index_page(scope):
	st.header('Ticker Index File')
	col1,col2,col3,col4,col5 = st.columns([3,2,2,2,3])
	with col1: st.success(('Ticker Index contains ( ' + str((len(scope.ticker_index_file))) + ' ) tickers'))
	with col2: download_ticker_index = st.button('Update Ticker Index File')
	with col3: show_ticker_index = st.button('Ticker Index File')
	with col4: show_industries = st.button('Industry Summary')
	
	st.markdown("""---""")
	
	if download_ticker_index:
		st.subheader('Downloading Ticker Master Data from https://asx.api.markitdigital.com and adding to the Ticker Index File')
		new_tickers_from_web(st.session_state)
	
	if show_ticker_index:
		st.subheader('Ticker Index File')
		st.dataframe(scope.ticker_index_file, 2000, 1200)

	if show_industries:
		industry_report(scope)

