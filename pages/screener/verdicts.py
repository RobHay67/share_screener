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

	first_row = True
	col1,col2,col3,col4,col5 = st.columns([2,1,7,1,1])
	# headings
	with col1:st.caption('Trial Name')
	with col2:st.caption('-- and ---')
	with col3:st.caption('Criteria (english explanation)')
	with col4:st.caption('Link to Definition')
	with col5:st.caption('Config Ref')
	st.divider()

	for trial in scope.trials['active_list']:

		connector = 'and ------- >'
		english_explanation = ''
		dict_of_values = scope.trials['config'][trial]['add_columns']
		column = dict_of_values['column'] if 'column' in dict_of_values else None
		trend = dict_of_values['trend'] if 'trend' in dict_of_values else None
		duration = dict_of_values['duration'] if 'duration' in dict_of_values else None
		timespan = dict_of_values['timespan'] if 'timespan' in dict_of_values else None
		periods = dict_of_values['periods'] if 'periods' in dict_of_values else None
		lookback_days = dict_of_values['lookback_days'] if 'lookback_days' in dict_of_values else None
		slow = dict_of_values['slow'] if 'slow' in dict_of_values else None
		signal = dict_of_values['signal'] if 'signal' in dict_of_values else None
		definition = scope.trials['config'][trial]['definition']
		print(definition)
		
		with col1: st.write(scope.trials['config'][trial]['short_name'])
		
		# st.write(scope.pages['ticker_values'])
		
		if trial in ['price_1', 'price_2', 'price_3']:
			column_name = scope.pages['ticker_values'][column]['long_english']
			english_explanation =  f"{column_name} is {trend}, {duration} of the previous {timespan} days"

		if trial in ['sma_1', 'sma_2', 'sma_3']:
			column_name = scope.pages['ticker_values'][column]['long_english']
			english_explanation =  f"{column_name} is trading {trend} the {periods} day Simple Moving Average (SMA)"

		if trial in ['stochastic_1', 'stochastic_2', 'stochastic_3']:

			english_explanation = 'STOCHASTIC'

		if trial in ['rsi_1', 'rsi_2']:
			# buy and sell zone

			
			column_name = scope.pages['ticker_values'][column]['long_english']
			english_explanation =  f"{column_name} is trending {trend} on the Relative Strength Index (RSI) having a lookback period of  {lookback_days} days."

		if first_row:
			connector= '....'
			first_row = False
		
		with col2: st.write(connector)
		with col3: st.write(english_explanation)
		with col4: st.write("[defintion]("+definition+")")
		with col5: st.write(trial)

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