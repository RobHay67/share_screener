# Display the Results from all the tests run on the ticker data
# - limit to tickers in the page worklist
# - ensure we have actually added columns to the ticker
# - expecting the verdicts to be stored in scope.tickers[ticker]['trials']['verdict']


import streamlit as st

from pages.websites.links import website_hyperlink
from pages.websites.links import link_to_app_button


def render_trial_verdicts(scope):
	tab_group_size 	= 10
	number_of_tabs 	= 30
	verdict_list 	= passing_verdict_list(scope)
	no_of_verdicts 	= len(verdict_list)

	if no_of_verdicts == 0:
		render_no_verdicts()
	elif no_of_verdicts > (tab_group_size * number_of_tabs):
		render_too_many_verdicts(no_of_verdicts, number_of_tabs, tab_group_size)
	else:
		render_passing_verdicts(scope, no_of_verdicts, tab_group_size, verdict_list)

	render_active_trials(scope)



# ===================== Abstracted Render Functions

def render_no_verdicts():
	st.error('No Passing Verdicts to Render')

def render_too_many_verdicts(no_of_verdicts, number_of_tabs, tab_group_size):
	st.error('Too many passing verdicts ('+str(no_of_verdicts)+') to render.')
	st.write('Maximum No of Tabs           = '+str(number_of_tabs))
	st.write('Maximum Verdicts in each tab = '+str(tab_group_size))
	st.write('Limit = Tabs x Verdict per Tab = '+str(tab_group_size * number_of_tabs))

def render_passing_verdicts(scope, no_of_verdicts, tab_group_size, verdict_list):
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
					
					company_name = scope.pages['ticker_search'][ticker]
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




def render_active_trials(scope):

	st.divider()
	st.subheader('Currently Active Trials / Tests')

	st.write('https://www.investopedia.com/articles/active-trading/041814/four-most-commonlyused-indicators-trend-trading.asp')

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([2,1,1,1,1,1,1,1])
	# headings
	with col1:st.caption('Trial Name')
	with col2:st.caption('Config Ref')
	with col3:st.caption('Trending')
	with col4:st.caption('On Column')
	with col5:st.caption('Duration / Periods')
	with col6:st.caption('Lookback Days')
	with col7:st.caption('Slow')
	with col8:st.caption('Timespan / Signal')
	st.divider()

	for trial in scope.trials['active_list']:

		with col1: st.write(scope.trials['config'][trial]['short_name'])
		with col2: st.write(trial)
		
		if trial in ['price_1', 'price_2', 'price_3']:
			with col3:st.write(scope.trials['config'][trial]['add_columns']['trend'])
			with col4:st.write(scope.trials['config'][trial]['add_columns']['column'])
			with col5:st.write(scope.trials['config'][trial]['add_columns']['duration'])
			with col6:st.caption('...')
			with col7:st.caption('...')
			with col8:st.write(scope.trials['config'][trial]['add_columns']['timespan'])
			
		if trial in ['sma_1', 'sma_2', 'sma_3']:
			with col3:st.write(scope.trials['config'][trial]['add_columns']['trend'])
			with col4:st.write(scope.trials['config'][trial]['add_columns']['column'])
			with col5:st.write(scope.trials['config'][trial]['add_columns']['periods'])
			with col6:st.caption('...')
			with col7:st.caption('...')
			with col8:st.caption('...')
		if trial in ['stochastic_1', 'stochastic_2', 'stochastic_3']:
			with col3:st.write(scope.trials['config'][trial]['add_columns']['trend'])
			with col4:st.caption('...')
			with col6:st.write(scope.trials['config'][trial]['add_columns']['lookback_days'])
			with col7:st.write(scope.trials['config'][trial]['add_columns']['slow'])
			with col8:st.write(scope.trials['config'][trial]['add_columns']['signal'])
		
		if trial in ['rsi_1', 'rsi_2']:
			with col3:st.write(scope.trials['config'][trial]['add_columns']['trend'])
			with col4:st.write(scope.trials['config'][trial]['add_columns']['column'])
			with col5:st.caption('...')
			with col6:st.write(scope.trials['config'][trial]['add_columns']['lookback_days'])
			with col7:st.caption('...')
			with col8:st.caption('...')

	st.subheader('Fliss Simple Strategy')
	st.write('Closing Price is up n times over the last x days')
	st.write('Volume is up n times over the last x days')




# ====================== helpers


def passing_verdict_list(scope):
	# Generate a list of tickers with an overall passing result
	page = scope.pages['display']
	verdict_list = []

	for ticker in scope.pages[page]['worklist']:
		# Only mined tickers can have verdicts
		if ticker in scope.pages[page]['tickers_used_by_page']:
			if scope.tickers[ticker][page]['verdict'] == 'pass':
				verdict_list.append(ticker)

	return verdict_list



def determine_tab_names(no_of_verdicts, tab_group_size):

	no_of_tabs = int(no_of_verdicts / tab_group_size)		
	if (no_of_verdicts % tab_group_size) > 0:no_of_tabs+=1
		
	list_of_tab_names = []
	for tab_no in range(no_of_tabs):
		list_of_tab_names.append(str(tab_no+1))
	
	return list_of_tab_names