import logging
import streamlit as st
from page.navigation.external_links import selectbox_external_link
from page.navigation.button_page_link import button_page_link
from page.navigation.button_external_link import button_external_link


def show_passing_verdicts(scope, no_of_verdicts, tab_group_size, verdict_list):
	logging.debug("show_passing_verdicts")
	page = scope.display['page']
	
	col1, col2 = st.columns([9,4]) #13

	with col1:st.subheader('Passing Trial Verdicts (' + str(no_of_verdicts) + ') passed')
	with col2:selectbox_external_link(scope)
	
	# Render the Results (in tabs because there could be lots)
	# Create List of Tab Names
	no_of_tabs = int(no_of_verdicts / tab_group_size)
	if (no_of_verdicts % tab_group_size) > 0:no_of_tabs+=1
	list_of_tab_names = []
	for tab_no in range(no_of_tabs):
		list_of_tab_names.append(str(tab_no+1))

	# Create Tabs and populate from verdicts
	tabs = st.tabs(list_of_tab_names)
	ticker_start = 0
	for i, tab in enumerate(tabs):
		tickers_for_tab = verdict_list[ticker_start:ticker_start+tab_group_size]
		ticker_start += tab_group_size
		with tab:
			for ticker in tickers_for_tab:
				col1,col2,col3,col4,col5,col6,col7 = st.columns([1,4,1,1,1,1,4]) #13
				
				company_name = scope.config['ticker_search'][ticker]
				with col1 :st.write(ticker)
				with col2 :st.write(company_name)
				with col3 :button_page_link(scope, 'chart', ticker)
				with col4 :button_page_link(scope, 'intraday', ticker)
				with col5 :button_page_link(scope, 'volume', ticker)
				with col6 :button_page_link(scope, 'research', ticker)
				if scope.page[page]['external_link'] != 'None':
					with col7 :button_external_link(scope, ticker)

