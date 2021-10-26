
import streamlit as st

def render_home_page(streamlit_session):
	st.title(streamlit_session.project_description)




# ===================================================================================================================================
# 
# Construct Ticker Lists for Analysis and Downloading validated share codes
#
# ===================================================================================================================================
def construct_list_of_share_codes(streamlit_session):
	st.info('Updating list of ticker codes')
	ticker_list = []
	
	# Most detailed takes precedece

	# Selected a ticker or tickers
	if len(streamlit_session.selected_tickers) != 0:
		for ticker in streamlit_session.selected_tickers:
			st.warning('adding this ticker to the Ticker List = ' + ticker )
			ticker_list += [ticker]	
		pass
	# Selected an Industry
	elif len(streamlit_session.selected_industry) != 0:
		for industry in streamlit_session.selected_industry:
			st.warning('adding ' + industry.upper() + ' to the ticker list' )
			tickers_in_industry_group_df = streamlit_session.share_index_file[streamlit_session.share_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	elif streamlit_session.selected_market != '< select entire market >':
		available_tickers_for_this_market = streamlit_session.share_index_file.index.values.tolist()
		ticker_list =  available_tickers_for_this_market
	else:
		st.warning('Failed to build a ticker list for the application')

	print ('ticker list = ', len(ticker_list))
	streamlit_session.ticker_list = ticker_list
	streamlit_session.ticker_list_needs_updating = False

	# st.info(streamlit_session.ticker_list)