
import streamlit as st

def render_home_page(scope):
	st.title(scope.project_description)




# ===================================================================================================================================
# 
# Construct Ticker Lists for Analysis and Downloading validated share codes
#
# ===================================================================================================================================
def construct_list_of_share_codes(scope):
	# print ( 'construct_list_of_share_codes - has been called')
	# print ('construct_list_of_share_codes > update_ticker_list_required = ', st.session_state.update_ticker_list_required)



	st.header('Ticker List - Add or Remove tickers from the Ticker List')
	ticker_list = []
	
	# ##############################
	# Most detailed takes precedece
	# ##############################

	# Selected a ticker or tickers
	if len(scope.selected_tickers) != 0:
		for ticker in scope.selected_tickers:
			st.success('adding ' + ticker + ' to the Ticker List' )
			ticker_list += [ticker]	
		pass

	# Selected an Industry
	elif len(scope.selected_industry) != 0:
		for industry in scope.selected_industry:
			st.success('adding ' + industry.upper() + ' to the Ticker List' )
			tickers_in_industry_group_df = scope.share_index_file[scope.share_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	
	# Selected an entire share market
	elif scope.selected_market != '< select entire market >':
		st.success('adding ' + scope.selected_market.upper() + ' to the Ticker List' )
		available_tickers_for_this_market = scope.share_index_file.index.values.tolist()
		ticker_list =  available_tickers_for_this_market
	else:
		st.error('All Tickers removed from Ticker List')

	scope.ticker_list = ticker_list
	scope.update_ticker_list_required = False

	st.subheader('Ticker List - after updating')
	ticker_list_message = ''
	for ticker in scope.ticker_list:
		ticker_list_message = ticker_list_message + ticker + ' - '
	st.success(ticker_list_message)

	st.info(('Number of tickers in Ticker List =  ( ' + str((len(scope.ticker_list))) + ' ) tickers'))

