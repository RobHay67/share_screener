import streamlit as st


from ticker_data import load_ticker_data_files, load_and_download_ticker_data

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Re-Usable Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_data_loader(scope, ticker_key):
	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 2.0, 2.0, 2.0, 1.8])
	
	dropdown_list = scope.dropdown_ticker
	prior_selection = scope.ticker[ticker_key]
	print(prior_selection)
	# index_of_ticker = dropdown_list.index(scope[ticker_variable])
	index_of_ticker = dropdown_list.index(prior_selection)

	with col1: 
		ticker = st.selectbox ( 'Select a Ticker', 
								dropdown_list, 
								index=index_of_ticker, 
								help='Choose a ticker for analysis. Start typing to jump within list'
								) 
	
	scope.ticker[ticker_key] = ticker							# Store the selection for next session
	
	if ticker != 'select a ticker':	
		
		with col3: st.download_days = st.number_input( 'number of days to download', 
														min_value=1, 
														max_value=6000, 
														value=1, 						# Default Value to display
														key='1')   
		
		with col4: load_tickers 	= st.button( 'Load File')
		with col4: download_tickers = st.button(('Add ' + str(int(st.download_days)) + ' days'))
		with col5: st.button('Clear All Messages')

		scope.ticker_list = [ticker]
		scope.download_industries = ['random_tickers']

		if load_tickers : 
			load_ticker_data_files(scope)

		if download_tickers:
			load_and_download_ticker_data(scope)

		# Add a Count of the rows in anyloaded dataframe
		if ticker in list(scope.share_data_files.keys()):
			no_of_rows = str(len(scope.share_data_files[ticker]))
		else: no_of_rows = '0'
		
		with col5: st.write(('No of Rows = ' + no_of_rows))
		

		st.header( scope.ticker_index_file.loc[ticker]['company_name'] )


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

