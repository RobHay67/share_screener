
import streamlit as st


from tickers.file import load_ticker_data_files
from tickers.download import load_and_download_ticker_data


def single_loader(scope, ticker_dropdown_selection):

	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 1.5, 1.5, 2.0, 3.0])
	
	dropdown_list = scope.dropdown_ticker
	previous_selection = scope.ticker[ticker_dropdown_selection]
	index_of_ticker = dropdown_list.index(previous_selection)

	with col1: 
		ticker = st.selectbox ( 'Select a Ticker', 
								dropdown_list, 
								index=index_of_ticker, 
								help='Choose a ticker for analysis. Start typing to jump within list'
								) 
	
	scope.ticker[ticker_dropdown_selection] = ticker		# Store the selection for next session
	
	if ticker != 'select a ticker':	
		with col3: st.download_days = st.number_input( 'download days', 
														min_value=1, 
														max_value=6000, 
														value=1, 						# Default Value to display
														key='1')   
		
		with col4: load_tickers 	= st.button( 'Load File')
		with col4: download_tickers = st.button(('Add ' + str(int(st.download_days)) + ' day'))
		with col5: st.button('Clear temp messages')

		scope.ticker_list = [ticker]
		scope.download_industries = ['random_tickers']

		if load_tickers : 
			load_ticker_data_files(scope)

		if download_tickers:
			load_and_download_ticker_data(scope)

		# Add a Count of the rows in anyloaded dataframe
		if ticker in list(scope.share_data_files.keys()):
			min_value = 1
			no_of_rows = len(scope.share_data_files[ticker])
			max_value = no_of_rows if no_of_rows > 0 else 0
			default_value = 300 if max_value > 300 else max_value
		else: 
			min_value,max_value,default_value,no_of_rows=0,0,0,0		
		
		with col5: st.write(('No of Loaded Rows = ' + str(no_of_rows)))
		

		# Render the Company Name and a Share Limiter control
		col1,col2,col3,col4 = st.columns([7.0, 1.7, 0.3, 3.0])
		with col1: st.header( scope.ticker_index_file.loc[ticker]['company_name'] )
		with col2: scope.analysis_limit_share_data = st.number_input( 	'limit analysis to X rows', 
																		min_value=min_value, 
																		max_value=max_value, 
																		value=default_value,
																		key='1')  
		with col3: scope.analysis_apply_limit = st.radio( 	"apply",
															('True','False'))
		




# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def multi_loader(scope):
	col1,col2,col3,col4,col5,col6 = st.columns([2,3,2,1.2,2,1.8])							# col2=4 is just a dummy to prevent the widget filling the whole screen

	dropdown_list_market = scope.dropdown_markets
	index_for_market = dropdown_list_market.index(scope.tickers_market)


	with col1: 
		market = st.selectbox( 		'Add a Market to Ticker List',
									dropdown_list_market, 
									index=index_for_market, 
									help='Select an Entire Share Market for Analysis',
									)
	with col2: 
		industries = st.multiselect(label='Add an Industry or Industries',
									options=scope.dropdown_industries,
									default=scope.tickers_industries,
									help='Quickly Select all tickers in a particular industry',
									)
	with col3: 
		tickers = st.multiselect( 	label='Add a Ticker or Tickers',
									options=scope.dropdown_tickers,
									default=scope.tickers_multi,
									help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list'
									)

	# Store the results so the list repopulate after re-render
	scope.tickers_market 	 = market
	scope.tickers_industries = industries
	scope.tickers_multi 	 = tickers
	construct_ticker_list(scope)

	print(scope.ticker_list)
	# print(scope.download_industries)
	
	if market != 'select entire market' or (len(industries) != 0) or len(tickers) != 0:

		with col4: load_tickers 	= st.button( 'Load Files')
		with col4: download_tickers = st.button(('Add  ' + str(int(scope.download_days)) + ' days'))
		with col5: st.button('Clear Messages')

		if load_tickers : 

			load_ticker_data_files(scope)

		if download_tickers:
		# 	print('running the download_tickers')
		# 	scope.download_industries = ['random_tickers']
			load_and_download_ticker_data(scope)

		# if ticker_end_date < analysis_begin_date or (ticker_begin_date > analysis_begin_date and ticker_end_date < analysis_end_date) or ticker_begin_date > analysis_end_date :



# ==============================================================================================================================================================
# Ticker List for Multi Ticker Analysis : Construct and Quick Show
# ==============================================================================================================================================================
def construct_ticker_list(scope):
	
	ticker_list = []
	relevant_industries = []
	
	# ################################################################################
	# Most detailed takes precedence
	# ################################################################################

	# Selected a ticker or tickers
	if len(scope.tickers_multi) != 0:
		for ticker in scope.tickers_multi:
			ticker_list.append(ticker)
			relevant_industries = ['random_tickers']
		pass
	# Selected an Industry
	elif len(scope.tickers_industries) != 0:
		for industry in scope.tickers_industries:
			tickers_in_industry_df = scope.ticker_index_file[scope.ticker_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_df.index.tolist()
			ticker_list += tickers_in_industry 
			relevant_industries.append(industry)
		pass
	
	# Selected an entire share market
	elif scope.tickers_market != 'select entire market':
		tickers_in_market = scope.ticker_index_file.index.values.tolist()
		ticker_list = tickers_in_market
		relevant_industries = ( list(scope.ticker_index_file['industry_group'].unique() ))
	
	scope.ticker_list = ticker_list
	scope.download_industries = relevant_industries