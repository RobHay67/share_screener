import streamlit as st

from ticker_data import load_ticker_data_files, load_and_download_ticker_data




# ==============================================================================================================================================================
# Web Page Render Controller
# ==============================================================================================================================================================
def render_analysis_multi_page(scope):
	st.title('Analysis - Multiple Tickers')

	render_selectors_for_analysis_multi(scope)

	# if len(scope.ticker_list) > 0:
	# 	st.info('We have some tickers')
	# else:
	# 	st.error('Add some tickers')


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_selectors_for_analysis_multi(scope):
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
									default=scope.tickers_selected,
									help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list'
									)

	# Store the results so the list repopulate after re-render
	scope.tickers_market 	 = market
	scope.tickers_industries = industries
	scope.tickers_selected 	 = tickers
	construct_ticker_list(scope)

	print(scope.ticker_list)
	print(scope.download_industries)
	
	if market != 'select entire market' or (len(industries) != 0) or len(tickers) != 0:

		with col4: load_tickers 	= st.button( 'Load Files')
		with col4: download_tickers = st.button(('Add  ' + str(int(st.download_days)) + ' days'))
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
	if len(scope.tickers_selected) != 0:
		for ticker in scope.tickers_selected:
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
		ticker_list.append(tickers_in_market)
		relevant_industries = ( list(scope.ticker_index_file['industry_group'].unique() ))
	
	scope.ticker_list = ticker_list
	scope.download_industries = relevant_industries












# def construct_list_of_ticker_codes(scope):
# 	st.header('Adding or Remove tickers from the Ticker List')
# 	ticker_list = []
	
# 	render_results( scope, passed='Added these selections ticker list > ', passed_2='na', failed='na' )

# 	# ##############################
# 	# Most detailed takes precedence
# 	# ##############################


# 	# Selected a ticker or tickers
# 	if len(scope.tickers_selected) != 0:
# 		for ticker in scope.tickers_selected:
# 			render_results( scope, ticker, result='passed' )
# 			ticker_list += [ticker]	
# 		pass

# 	# Selected an Industry
# 	elif len(scope.tickers_industries) != 0:
# 		for industry in scope.tickers_industries:
# 			render_results( scope, industry.upper(), result='passed' )
# 			tickers_in_industry_group_df = scope.ticker_index_file[scope.ticker_index_file['industry_group'] == industry ]
# 			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
# 			ticker_list += tickers_in_industry 
# 		pass
	
# 	# Selected an entire share market
# 	elif scope.tickers_market != 'select entire market':
# 		render_results( scope, scope.tickers_market.upper(), result='passed' )
# 		available_tickers_for_this_market = scope.ticker_index_file.index.values.tolist()
# 		ticker_list =  available_tickers_for_this_market
# 	else:
# 		st.error('All Tickers removed from Ticker List')

# 	render_results(scope, 'Finished', final_print=True )

# 	scope.tickers_for_multi = ticker_list
# 	scope.tickers_update_list = False

# 	st.markdown("""---""")

# 	st.subheader('Ticker List - after adding dropdown selections')
# 	ticker_list_message = ''
# 	for ticker in scope.tickers_for_multi:
# 		ticker_list_message = ticker_list_message + ticker + ' - '
# 	st.success(ticker_list_message)

# 	st.write(('Number of tickers in Ticker List =  ( ' + str((len(scope.tickers_for_multi))) + ' ) tickers'))