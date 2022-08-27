import streamlit as st

from widgets.drill import drill_website_button
from widgets.drill import drill_app_button


def render_trial_results(scope):

	st.write('**Trial Verdicts = Passed**')

	app = scope.apps['display_app']
	group_size = 10
	tab_limit = 10

	# Generate a list of tickers with an overall passing result
	verdict_list = []
	for ticker in scope.apps[app]['worklist']:
		# Only mined tickers can have a verdict
		if ticker in scope.apps[app]['mined_tickers']:
			if scope.tickers[ticker]['trials']['verdict'] == 'pass':
				verdict_list.append(ticker)
	no_of_verdicts = len(verdict_list)

	
	if no_of_verdicts > (group_size * tab_limit):
		# Dont render more than say 100 Tickers
		st.error('Too many passing verdicts to render (' + str(no_of_verdicts) + ')')
	else:
		# Render the Results
		no_of_tabs = int(no_of_verdicts / group_size)		
		if (no_of_verdicts % group_size) > 0:no_of_tabs+=1
			
		tab_list = []
		for tab_no in range(no_of_tabs):
			tab_list.append('Group ' + str(tab_no+1))
			
		# Create Tabs and populate from verdicts
		tabs = st.tabs(tab_list)
		ticker_start = 0
		for i, tab in enumerate(tabs):
			tickers_for_tab = verdict_list[ticker_start:ticker_start+group_size]
			ticker_start += group_size
			with tab:
				for ticker in tickers_for_tab:
					col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns([1,4,1,1,1,1,1,1,1,1])
					company_name = scope.ticker_search[ticker]

					with col1 : st.write(ticker)
					with col2 : st.write(company_name)
					with col3 : drill_app_button(scope, 'single', ticker)
					with col4 : drill_app_button(scope, 'intraday', ticker)
					with col5 : drill_app_button(scope, 'volume', ticker)
					with col6 : drill_app_button(scope, 'research', ticker)
					with col7 : drill_website_button(scope, 'asx', ticker)
					with col8 : drill_website_button(scope, 'google', ticker)
					with col9 : drill_website_button(scope, 'yahoo', ticker)
					with col10 : drill_website_button(scope, 'marketindex', ticker)








