import streamlit as st




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_download_message(scope):

	if scope.download['yf_batch_industry'] == 'random_tickers':
		download_message = (	scope.download['yf_batch_ticker_string'])
	else:
		download_message = (
								scope.download['yf_batch_industry'] + 
								' ( batch ' + 
								str(scope.download['yf_batch_no']+1) + 
								' of ' + 
								str(len(scope.download['yf_download_these_industries'])) + 
								' )' 
							)
	
	st.write(download_message)

