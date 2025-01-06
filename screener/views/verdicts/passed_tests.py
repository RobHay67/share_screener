import streamlit as st
from app.views.header.links import link_to_app_button
from app.views.header.links import website_hyperlink


def passing_verdict_list(scope):
	# Generate a list of tickers with an overall passing result
	page = scope.config['display']
	verdict_list = []

	for ticker in scope.page[page]['worklist']:
		# Only mined tickers can have verdicts
		if ticker in scope.page[page]['loaded_ticker_list']:
			if scope.tickers[ticker][page]['verdict'] == 'pass':
				verdict_list.append(ticker)

	return verdict_list


def show_passing_verdicts(scope, no_of_verdicts, tab_group_size, verdict_list):
		# Render the Results (in tabs and there could be lots)
		st.subheader('Passing Test Results       (' + str(no_of_verdicts) + ') passed')
		
		list_of_tab_names = determine_tab_names(no_of_verdicts, tab_group_size)
		
		# Create Tabs and populate from verdicts
		tabs = st.tabs(list_of_tab_names)
		ticker_start = 0
		for i, tab in enumerate(tabs):
			tickers_for_tab = verdict_list[ticker_start:ticker_start+tab_group_size]
			ticker_start += tab_group_size
			with tab:
				for ticker in tickers_for_tab:
					col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13 = st.columns([1,4,1,1,1,1,1,1,1,1,1,1,1])
					
					company_name = scope.config['ticker_search'][ticker]
					with col1 :st.write(ticker)
					with col2 :st.write(company_name)
					with col3 :link_to_app_button(scope, 'chart', ticker)
					with col4 :link_to_app_button(scope, 'intraday', ticker)
					with col5 :link_to_app_button(scope, 'volume', ticker)
					with col6 :link_to_app_button(scope, 'research', ticker)
					with col7 :website_hyperlink(scope, 'eTrade', ticker)
					with col8 :website_hyperlink(scope, 'asx', ticker)
					with col9 :website_hyperlink(scope, 'google', ticker)
					with col10:website_hyperlink(scope, 'yahoo', ticker)
					with col11:website_hyperlink(scope, 'market index', ticker)
					with col12:website_hyperlink(scope, 'hot copper', ticker)
					with col13:website_hyperlink(scope, 'market watch', ticker)



def determine_tab_names(no_of_verdicts, tab_group_size):

	no_of_tabs = int(no_of_verdicts / tab_group_size)		
	if (no_of_verdicts % tab_group_size) > 0:no_of_tabs+=1
		
	list_of_tab_names = []
	for tab_no in range(no_of_tabs):
		list_of_tab_names.append(str(tab_no+1))
	
	return list_of_tab_names