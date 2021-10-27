
import streamlit as st

def render_home_page(scope):
	st.title(scope.project_description)




# ===================================================================================================================================
# 
# Construct Ticker Lists for Analysis and Downloading validated share codes
#
# ===================================================================================================================================
def construct_list_of_share_codes(scope):
	st.info('Updating list of ticker codes')
	ticker_list = []
	
	# Most detailed takes precedece

	# Selected a ticker or tickers
	if len(scope.selected_tickers) != 0:
		for ticker in scope.selected_tickers:
			st.warning('adding this ticker to the Ticker List = ' + ticker )
			ticker_list += [ticker]	
		pass
	# Selected an Industry
	elif len(scope.selected_industry) != 0:
		for industry in scope.selected_industry:
			st.warning('adding ' + industry.upper() + ' to the ticker list' )
			tickers_in_industry_group_df = scope.share_index_file[scope.share_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	elif scope.selected_market != '< select entire market >':
		available_tickers_for_this_market = scope.share_index_file.index.values.tolist()
		ticker_list =  available_tickers_for_this_market
	else:
		st.warning('Failed to build a ticker list for the application')

	print ('ticker list = ', len(ticker_list))
	scope.ticker_list = ticker_list
	scope.ticker_list_needs_updating = False

	# st.info(scope.ticker_list)