import streamlit as st

# from ticker_data import load_ticker_data_files, load_and_download_ticker_data

# from ticker.tickers.file import load_ticker_data_files
# from ticker.tickers.download import load_and_download_ticker_data





















# def construct_list_of_ticker_codes(scope):
# 	st.header('Adding or Remove tickers from the Ticker List')
# 	ticker_list = []
	
# 	render_results( scope, passed='Added these selections ticker list > ', passed_2='na', failed='na' )

# 	# ##############################
# 	# Most detailed takes precedence
# 	# ##############################


# 	# Selected a ticker or tickers
# 	if len(scope.selected_tickers) != 0:
# 		for ticker in scope.selected_tickers:
# 			render_results( scope, ticker, result='passed' )
# 			ticker_list += [ticker]	
# 		pass

# 	# Selected an Industry
# 	elif len(scope.selected_industries) != 0:
# 		for industry in scope.selected_industries:
# 			render_results( scope, industry.upper(), result='passed' )
# 			tickers_in_industry_group_df = scope.ticker_index_file[scope.ticker_index_file['industry_group'] == industry ]
# 			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
# 			ticker_list += tickers_in_industry 
# 		pass
	
# 	# Selected an entire share market
# 	elif scope.selected_market != 'select entire market':
# 		render_results( scope, scope.selected_market.upper(), result='passed' )
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