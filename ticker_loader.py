import streamlit as st


from ticker_data import load_ticker_data_files, load_and_download_ticker_data



		# scope.ticker				={
		# 								'company_profile':'select a ticker',
		# 								'volume_predict' :'select a ticker',
		# 								'intraday'		 :'select a ticker',
		# 								'single'		 :'select a ticker',
		# 							}
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Re-Usable Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_selectors_for_single_ticker(scope, ticker_key):
	col1,col2,col3,col4,col5 = st.columns([2,2,1.2,2,4.8])
	
	dropdown_list = scope.dropdown_ticker
	prior_selection = scope.ticker[ticker_key]
	print(prior_selection)
	# index_of_ticker = dropdown_list.index(scope[ticker_variable])
	index_of_ticker = dropdown_list.index(prior_selection)

	with col1: 
		ticker = st.selectbox ( 'Select Ticker', 
								dropdown_list, 
								index=index_of_ticker, 
								help='Select a ticker. Start typing to jump within list'
								) 
	
	scope.ticker[ticker_key] = ticker							# Store the selection for next session
	# ticker_variable = ticker									# Store the selection for next session
	# scope[ticker_variable] = ticker									# Store the selection for next session
	
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


def render_ticker_data_file(scope, ticker): # WIP
	st.markdown('##### Loaded and / or Downloaded share data.')

	# ticker = scope.ticker['research']

	if ticker in list(scope.share_data_files.keys()):
		ticker_data_file = scope.share_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=ticker)
		my_expander.dataframe(ticker_data_file, 2000, 2000)	
	else:
		st.error('Load / Download some ticker data')

