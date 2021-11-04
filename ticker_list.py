
import streamlit as st

from browser import render_results





# def render_home_page(scope):
# 	st.title(scope.project_description)


def render_ticker_list(scope):
	st.header('Ticker List')
	st.subheader('target tickers for analysis')
	st.write('use sidebar to add tickers to this list)')
	ticker_list_message = ''
	for count, ticker in enumerate(scope.tickers_for_multi):
		ticker_list_message = ticker_list_message + ticker
		if count < len(scope.tickers_for_multi) - 1:
			ticker_list_message += '  '

	st.success(ticker_list_message)

# ===================================================================================================================================
# 
# Construct Ticker Lists for Analysis and Downloading validated share codes
#
# ===================================================================================================================================
def construct_list_of_share_codes(scope):
	st.header('Adding or Remove tickers from the Ticker List')
	ticker_list = []
	
	render_results( scope, passed='Added these selections ticker list > ', passed_2='na', failed='na' )

	# ##############################
	# Most detailed takes precedence
	# ##############################

	
	# A single ticker
	if scope.chosen_single_ticker != '< not selected >':
		ticker = scope.chosen_single_ticker
		render_results( scope, ticker, result='passed' )
		ticker_list += [ticker]

		if ticker in scope.share_data_loaded_list:
			keep_exisiting_data = scope.share_data_files[ticker]
			scope.share_data_files = {}
			scope.share_data_files[ticker] = keep_exisiting_data
		else:
			scope.share_data_files = {}  # empty the loaded data

	# Selected a ticker or tickers
	elif len(scope.chosen_tickers) != 0:
		for ticker in scope.chosen_tickers:
			render_results( scope, ticker, result='passed' )
			ticker_list += [ticker]	
		pass

	# Selected an Industry
	elif len(scope.chosen_industries) != 0:
		for industry in scope.chosen_industries:
			render_results( scope, industry.upper(), result='passed' )
			tickers_in_industry_group_df = scope.share_index_file[scope.share_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	
	# Selected an entire share market
	elif scope.chosen_market != '< select entire market >':
		render_results( scope, scope.selected_market.upper(), result='passed' )
		available_tickers_for_this_market = scope.share_index_file.index.values.tolist()
		ticker_list =  available_tickers_for_this_market
	else:
		st.error('All Tickers removed from Ticker List')

	render_results(scope, 'Finished', final_print=True )

	scope.tickers_for_multi = ticker_list
	scope.update_ticker_list_required = False

	st.markdown("""---""")

	st.subheader('Ticker List - after adding dropdown selections')
	ticker_list_message = ''
	for ticker in scope.tickers_for_multi:
		ticker_list_message = ticker_list_message + ticker + ' - '
	st.success(ticker_list_message)

	st.write(('Number of tickers in Ticker List =  ( ' + str((len(scope.tickers_for_multi))) + ' ) tickers'))


