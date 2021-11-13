



import streamlit as st



from ticker.list import construct_ticker_list


from ticker.load import load_ticker_data_files
from ticker.download import load_and_download_ticker_data

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Reports
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def ticker_data_files(scope): # DONE
	st.header('Loaded and Downloaded share data.')
	list_of_loaded_tickers = list(scope.share_data_files.keys())
	list_of_loaded_tickers.sort()

	for ticker in list_of_loaded_tickers:
		ticker_data_file = scope.share_data_files[ticker]
		ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)
		my_expander = st.expander(label=ticker)
		my_expander.dataframe(ticker_data_file, 2000, 2000)	


def ticker_list(scope): # DONE
	st.header('Ticker List')
	st.subheader('target tickers for analysis')
	st.write('use sidebar to add tickers to this list)')

	ticker_list_message = ''
	for count, ticker in enumerate(scope.ticker_list):
		ticker_list_message = ticker_list_message + ticker
		if count < len(scope.ticker_list) - 1:
			ticker_list_message += '  '

	st.success(ticker_list_message)





# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load a Single Ticker
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def single_loader(scope, page):

	# Set up the initial state for the dropdown list
	ticker_for_page = scope.ticker_list[page]
	index_for_page_ticker = scope.dropdown_ticker.index(ticker_for_page)

	# render the selector defalted to the stored ticker for this page
	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 1.5, 1.5, 2.0, 3.0])
	with col1: 
		ticker = st.selectbox ( label='Select a Ticker', 
								options=scope.dropdown_ticker,
								index=scope.dropdown_ticker.index(ticker_for_page), 
								help='Choose a ticker for analysis. Start typing to jump within list',
								key=page,
								) 
	print('page <', page, '> prior ticker = ', ticker_for_page, '(', index_for_page_ticker,') current selection = ', ticker)
	scope.ticker_list[page] = ticker		# Store the selection so we can easily swap pages
	
	if ticker != 'select a ticker':	
		with col3: st.download_days = st.number_input( 'download days', 
														min_value=1, 
														max_value=6000, 
														value=1, 						# Default Value to display
														key='1')   
		
		with col4: load_tickers 	= st.button( 'Load File')
		with col4: download_tickers = st.button(('Add ' + str(int(st.download_days)) + ' day'))
		with col5: st.button('Clear temp messages')

		scope.download_industries = ['random_tickers']									# used for y_finance downloading

		if load_tickers : 
			load_ticker_data_files(scope)												# TODO - this should default to the single loader - why the general one?

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
		

		# Render the Company Name and a Share Limiter controler
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
# Load a batch of tickers
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






