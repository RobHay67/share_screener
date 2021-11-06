
import streamlit as st

from ticker_data import construct_list_of_ticker_codes

def render_multi_analysis_page(scope):
	st.title('Analysis - Multiple Tickers')

	render_selectors_for_multi_analysis(scope)


	if len(scope.tickers_for_multi) > 0:
		st.info('We have some tickers')
	else:
		st.error('Add some tickers')




# Select Tickers -----------------------------------------------------------------------------------------------
# def tickers_update_list(): st.session_state.tickers_update_list = True
# st.sidebar.subheader('Choose Tickers (lowest takes precedence)')
# market   = st.sidebar.selectbox  ('Choose a Market'  	, st.session_state.dropdown_markets   , on_change=tickers_update_list, help='Select an Entire Share Market for Analysis')
# industry = st.sidebar.multiselect('Choose Industries'	, st.session_state.dropdown_industries, on_change=tickers_update_list, help='Quickly Select all tickers in a particular industry')
# tickers  = st.sidebar.multiselect('Choose Tickers'   	, st.session_state.dropdown_tickers   , on_change=tickers_update_list, help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list') 
# ticker   = st.sidebar.selectbox  ('Choose a lone Ticker', st.session_state.dropdown_single_ticker   , on_change=tickers_update_list, help='Select a single ticker only. Start typing to jump within list') 

# Update the ticker list if required (selector box has changed)
# if st.session_state.tickers_update_list:
# 	st.session_state.tickers_market = market
# 	st.session_state.tickers_industries = industry
# 	st.session_state.tickers_selected = tickers
#	st.session_state.chosen_single_ticker = ticker
# 	construct_list_of_ticker_codes(st.session_state)

def tickers_update_list(): 
	st.session_state.tickers_update_list = True


def render_selectors_for_multi_analysis(scope):
	col1,col2,col3,col4 = st.columns([2,3,2,5])							# col2=4 is just a dummy to prevent the widget filling the whole screen

	dropdown_list_market = scope.dropdown_markets
	index_for_market = dropdown_list_market.index(scope.tickers_market)


	with col1: 
		market = st.selectbox( 		'Add a Market to Ticker List',
									dropdown_list_market, 
									on_change=tickers_update_list,
									index=index_for_market, 
									help='Select an Entire Share Market for Analysis',
									)
	with col2: 
		industry = st.multiselect(	label='Add an Industry or Industries',
									options=scope.dropdown_industries,
									default=scope.tickers_industries,
									on_change=tickers_update_list,
									help='Quickly Select all tickers in a particular industry',
									)
	with col3: 
		tickers = st.multiselect( 	label='Add a Ticker(s) to the Ticker List',
									options=scope.dropdown_tickers,
									default=scope.tickers_selected,
									on_change=tickers_update_list,
									help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list'
									)

	if st.session_state.tickers_update_list:
		st.session_state.tickers_market = market
		st.session_state.tickers_industries = industry
		st.session_state.tickers_selected = tickers
		construct_list_of_ticker_codes(st.session_state)


# the loader and downloader needs to set the following :

# scope.download_groups_for_y_finance = ['random_tickers']

# if scope.tickers_market != 'select entire market':
# 	scope.download_groups_for_y_finance = ( list(scope.ticker_index_file['industry_group'].unique() ))
# elif len(scope.tickers_industries) != 0:
# 	scope.download_groups_for_y_finance = scope.tickers_industries				# TODO - test this one Rob as I needed to change it
# elif len(scope.tickers_selected) != 0:
# 	scope.download_groups_for_y_finance.append('random_tickers')







# def update_ticker_list():
# 	print( 'I have been called to update the ticker list')
# 	print( 'Industries = ', st.session_state.tickers_industries )
# 	construct_list_of_ticker_codes(st.session_state)



	# with col1: 
	# 	ticker = st.selectbox ( 'Select Ticker', 
	# 							dropdown_list, 
	# 							index=index_of_ticker, 
	# 							help='Select a ticker. Start typing to jump within list'
	# 							) 