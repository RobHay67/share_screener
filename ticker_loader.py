import streamlit as st


from ticker_data import load_ticker_data_files, load_and_download_ticker_data




# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Re-Usable Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_selectors_for_single_ticker(scope, ticker_variable):
	col1,col2,col3,col4,col5 = st.columns([2,2,1.2,2,4.8])
	
	dropdown_list = scope.dropdown_ticker
	index_of_ticker = dropdown_list.index(scope[ticker_variable])

	with col1: 
		ticker = st.selectbox ( 'Select Ticker', 
								dropdown_list, 
								index=index_of_ticker, 
								help='Select a ticker. Start typing to jump within list'
								) 
	

	scope[ticker_variable] = ticker									# Store the selection for next session
	
	if ticker != 'select a ticker':	
		st.header( scope.ticker_index_file.loc[ticker]['company_name'] )	

		with col3: load_tickers 	= st.button( 'Load File')
		with col3: download_tickers = st.button(('Add ' + str(int(st.download_days)) + ' days'))

		with col4: st.button('Clear Messages')

		scope.ticker_list = [ticker]
		# TODO - we need to set a flag that resets the ticker list button in the sidebar
		scope.download_industries = ['random_tickers']

		if load_tickers : 
			load_ticker_data_files(scope)

		if download_tickers:
			load_and_download_ticker_data(scope)



