
import streamlit as st
from reports import output_results_to_browser

def render_home_page(scope):
	st.title(scope.project_description)




# ===================================================================================================================================
# 
# Construct Ticker Lists for Analysis and Downloading validated share codes
#
# ===================================================================================================================================
def construct_list_of_share_codes(scope):
<<<<<<< HEAD
	# print ( 'construct_list_of_share_codes - has been called')
	# print ('construct_list_of_share_codes > update_ticker_list_required = ', st.session_state.update_ticker_list_required)



	st.header('Ticker List - Add or Remove tickers from the Ticker List')
=======
	st.header('Adding or Remove tickers from the Ticker List')
>>>>>>> download_tickers
	ticker_list = []
	
	output_results_to_browser( scope, passed='Added these selections ticker list > ', passed_2='na', failed='na' )

	# ##############################
	# Most detailed takes precedence
	# ##############################

	# Selected a ticker or tickers
	if len(scope.selected_tickers) != 0:
		for ticker in scope.selected_tickers:
			output_results_to_browser( scope, ticker, result='passed' )
			ticker_list += [ticker]	
		pass

	# Selected an Industry
	elif len(scope.selected_industry) != 0:
		for industry in scope.selected_industry:
			output_results_to_browser( scope, industry.upper(), result='passed' )
			tickers_in_industry_group_df = scope.share_index_file[scope.share_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	
	# Selected an entire share market
	elif scope.selected_market != '< select entire market >':
		output_results_to_browser( scope, scope.selected_market.upper(), result='passed' )
		available_tickers_for_this_market = scope.share_index_file.index.values.tolist()
		ticker_list =  available_tickers_for_this_market
	else:
		st.error('All Tickers removed from Ticker List')

	output_results_to_browser(scope, 'Finished', final_print=True )

	scope.ticker_list = ticker_list
	scope.update_ticker_list_required = False

	st.markdown("""---""")

	st.subheader('Ticker List - after adding dropdown selections')
	ticker_list_message = ''
	for ticker in scope.ticker_list:
		ticker_list_message = ticker_list_message + ticker + ' - '
	st.success(ticker_list_message)

	st.write(('Number of tickers in Ticker List =  ( ' + str((len(scope.ticker_list))) + ' ) tickers'))


