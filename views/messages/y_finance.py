import streamlit as st




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_download_message(scope):

	col1,col2,col3,col4 = st.columns([5.5,1.5,1,4])


	yf_ticker_list = scope.yf['batch_ticker_string'].split(' ')
	no_of_tickers = len(yf_ticker_list)

	if scope.yf['batch_industry'] == 'random_tickers':
		batch_no = 'Manually Selected Tickers'		
	else:
		batch_no = (
					' ( batch ' + 
					str(scope.yf['batch_no']+1) + 
					' of ' + 
					str(len(scope.yf['download_these_industries'])) + 
					' )'
					)

	with col2:
		st.write(batch_no)
	with col3:
		st.write('tickers = ' + str(no_of_tickers))
	with col4:
		st.write(scope.yf['batch_industry'])


def render_download_complete_message(scope):

	col1,col2,col3,col4 = st.columns([5.5,1.5,1,4])

	with col2:
		st.write('--------')
		st.write('complete')
	with col3:
		st.write('---------------')
		st.write('tickers = ' + str(len(scope.yf['ticker_list'])))
	with col4:
		st.write('-----------------')
		st.write('Download Complete')