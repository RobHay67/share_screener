
import streamlit as st

def render_home_page(streamlit_session):
	st.title(streamlit_session.project_description)




# ===================================================================================================================================
# 
# Construct Ticker Lists for Analysis and Downloading validated share codes
#
# ===================================================================================================================================
def construct_list_of_share_codes(session_state):
	st.info('Updating list of ticker codes')
	ticker_list = []

	print ('construct_list_of_share_codes = ', len(st.session_state.ticker_list))
	
	# Most detailed takes precedece
	if len(session_state.selected_tickers) != 0:
		print('this many selected tickers = ', len(session_state.selected_tickers))
		for ticker in session_state.selected_tickers:
			st.warning('adding this ticker to the Ticker List = ' + ticker )
			ticker_list += [ticker]	
		pass
	elif len(session_state.selected_industry) != 0:
		for industry in session_state.selected_industry:
			st.warning('adding ' + industry.upper() + ' to the ticker list' )
			tickers_in_industry_group_df = session_state.share_index_file[session_state.share_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	elif session_state.selected_industry != 'Select an Industry':
		available_market_codes = session_state.share_index_file.index.values.tolist()
		ticker_list =  available_market_codes
	else:
		st.warning('Could not build a ticker list for analyis')

	print ('ticker list = ', len(ticker_list))
	session_state.ticker_list = ticker_list
	session_state.ticker_list_needs_updating = False