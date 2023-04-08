# Display the Results from all the tests run on the ticker data
# - limit to tickers in the page worklist
# - ensure we have actually added columns to the ticker
# - expecting the verdicts to be stored in scope.tickers[ticker]['trials']['verdict']


import streamlit as st

from pages.widgets.links import website_hyperlink
from pages.widgets.links import link_to_app_button


def render_trial_verdicts(scope):
	
	group_size = 10
	number_of_tabs = 30
	verdict_list = passing_verdict_list(scope)
	no_of_verdicts = len(verdict_list)

	st.subheader('Passing Test Results       (' + str(no_of_verdicts) + ') passed')
	
	if no_of_verdicts == 0:
		st.warning('No Passing Verdicts to Render')
	elif no_of_verdicts > (group_size * number_of_tabs):
		st.error('Too many passing verdicts ('+str(no_of_verdicts)+') to render.')
		st.write('Maximum No of Tabs           = '+str(number_of_tabs))
		st.write('Maximum Verdicts in each tab = '+str(group_size))
		st.write('Limit = Tabs x Verdict per Tab = '+str(group_size * number_of_tabs))
	else:
		# Render the Results
		no_of_tabs = int(no_of_verdicts / group_size)		
		if (no_of_verdicts % group_size) > 0:no_of_tabs+=1
			
		tab_list = []
		for tab_no in range(no_of_tabs):
			tab_list.append(str(tab_no+1))

		# Create Tabs and populate from verdicts
		tabs = st.tabs(tab_list)
		ticker_start = 0
		for i, tab in enumerate(tabs):
			tickers_for_tab = verdict_list[ticker_start:ticker_start+group_size]
			ticker_start += group_size
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




def passing_verdict_list(scope):
	# Generate a list of tickers with an overall passing result
	page = scope.display_page
	verdict_list = []

	for ticker in scope.pages[page]['worklist']:
		# Only mined tickers can have verdicts
		if ticker in scope.pages[page]['tickers_with_add_cols']:
			if scope.tickers[ticker][page]['verdict'] == 'pass':
				verdict_list.append(ticker)

	return verdict_list



