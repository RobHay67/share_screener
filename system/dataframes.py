import streamlit as st

from index.load import load_ticker_index_file

# ticker_index 			DataFrame  				A list of all tickers available to the application
# ticker_data_files		dict of DataFrames		All Share Data files indexed by Ticker Code
# ticker_data			DataFrame				A Specific Ticker Extract from the ticker_data_files which can be manipulated - ie moving averages




def scope_dataframes(scope):
	# Primary Application Objects
	scope.ticker_index = {}						# was previous ticker_index_file
	load_ticker_index_file(scope)
	scope.ticker_data_files 			= {}		# TODO rename to ticker_data_files


# render_ticker_index
def render_ticker_index(scope):
	# ticker_index_report
	col1,col2 = st.columns([6,2])
	
	with col1: st.subheader('Ticker Index File')
	with col2: st.write('< ticker_index >')

	st.dataframe(scope.ticker_index, 2000, 1200)


