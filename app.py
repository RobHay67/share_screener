# ------------------------------------------------- Execute Application
# pipenv shell
# streamlit run app.py
# ------------------------------------------------- GitHub
# git push -u origin <branch>
# git branch -d <branch>   will delete local branch
# ------------------------------------------------- Package Management
# pip3 install --user --upgrade django
# ------------------------------------------------- Pipenv
# cd into project folder 
# activate Pipenv 	- pipenv shell
# deactivate env	- exit
# install packages  - pipenv install
# add a package 	- pipenv install django
# upgrade package	- 
# specify ver   	- pipenv install mplfinance==0.12.7a5
# latest ver		- pipenv update pandas
# delete pkg		- pipenv uninstall django
# -------------------------------------------------

import streamlit as st

# Testing Code - TODO - delete on Final Release
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



from config.controller import set_scope
from apps.sidebar.sidebar import render_sidebar
from apps.controller import render_selected_page

print ( '\033[94m' + 'Application Re-Rendering Now ' + '>'*50 + '\033[0m')


scope = set_scope(st.session_state)


render_sidebar(scope)
render_selected_page(scope)




Data_frame = 'DataFrame'

# Status
replace_columns = True

scope_data = {
	'tickers':	{
					'CBA':	{
								'df':Data_frame,
								'replace_app_dfs':True, 		# True or False
								'replace_columns':True,			# this could serve as a shortcut to save iterating through all the page config
								# pages/apps
								'apps': {
											'single':	{
															'df':Data_frame,
															# 'replace_app_dfs':True, 		# Not needed - do at header only
															'candlestick':replace_columns,
															'macd': replace_columns, 
															'macd_vol': replace_columns, 
															'rsi': replace_columns, 
															'vol_osssy': False, 
															'stochastic': replace_columns, 
															'sma_1': replace_columns, 
															'sma_2': False, 
															'sma_3': False, 
															'ema_1': False, 
															'ema_2': False, 
															'ema_3': False, 
															'bollinger_bands': False, 
															'dividends': replace_columns, 
															'candlestick': replace_columns, 
															'scatter': False, 
															'bar': False, 
															'line': replace_columns, 
															'heiken_ashi': False, 
															'volume': replace_columns, 
															'vol_per_minute': False, 
															'vac': False,
															'announcements': False, 
															'ichi_moku': False, 
															'ichi_moku_daily': False
														},
											'screener':	{
															'df':Data_frame,
															# 'replace_app_dfs':True, 		# Not needed - do at header only
															'trend_open': False, 
															'trend_high': replace_columns, 
															'trend_low': False, 
															'trend_close': replace_columns, 
															'trend_volume': False,
														},
										},
							},
				},
	}


print(scope.pages['templates']['charts'])
# so when we load a file - we just add the appropriate page config from the defaults. The true will signifiy that the 
# columns need replacing. After replacing, set the status to false to prevent further updates




# Events that require the dataframe or the page columns to be replaced or recalculated
#		Transaction							which ticker(s)				app dataframe		app dataframe columns
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# a)	Load ticker data file				Single Ticker				xReplace All Dfs 	Replace ALL Columns
# b)	Change the < page_row_limit >		EVERY Ticker				xReplace All Dfs 	Replace ALL Columns
# c)	Activate an chart/overlay/test		Every Ticker Using object	ignore				Replace cols for this object
# d)	Deactive a chart/overlay/test		ignore						ignore				ignore
# g)	Change Value in chart/overlay/test	Every Ticker Using object	ignore				Replace cols for this object


# Current Page and usage of column adders
# APP		Objects
# --------------------------------------------
# single	charts and overlays
# intraday	none
# volume	none
# research	none
# screener	tests











# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load ticker for cba						T-r_df	T-r_dfl ------			------			-------		-------			-------		= refresh the tickers that have changed
#											T-r_col	T-r_col ------			------			-------		-------			-------
# Download new ticker for cba + NAB			T-r_df	T-r_dfl ------			-------			T-r_df		T-r_df			-------		= refresh the tickers that have changed
#											T-r_col	T-r_col ------			------			-------		-------			-------
# Change the < page_row_limit >				T-r_all T-r_all T-r_all			T-r_all			T-r_all		T-r_all			T-r_all		= refresh all tickers and rerun all active add_cols
# Activate overlay or 2nd chart				------	------	------			T-r_col			T-r_col		T-r_col			T-r_col		= recalculate the specific add_cols only	for NON screener pages							
# Update value in overlay or 2nd chart		------	------	------			T-r_col			T-r_col		T-r_col			T-r_col		= recalculate the specific add_cols only	for NON screener pages	
# Activate a col_adder						T-r_col	T-r_col	T-r_col			-------			-------		-------			-------		= recalculate the specific add_cols only	for screener page
# Change col_adder value 					T-r_col	T-r_col	T-r_col			-------			-------		-------			-------		= recalculate the specific add_cols only	for screener page
# Replace the page_df on single page		R-r_df	-------	-------			-------			-------		-------			-------
# Rerun the column adder single page		R-r_col	-------	-------			-------			-------		-------			-------		

# set_replace_df_status_for_ticker
# set_replace_df_status_for_all_tickers
# set_replace_col_status_for_ticker
# set_replace_col_status_for_col_adder
# set_replace_cols_status_for_all_tickers
# set_replace_col_adder_status_for_ticker_and_page
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# KEY		Description				Pages		Tickers		Dataframe									add_columns	replace_cols							Replace DF Func		Replace Cols Func		
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# T-r_df 	tag to replace df		All			Specific	set_replace_df_status_for_ticker			------------------------------------------------	replace_dfs			---------------------	
# T-r_col	tag to add_cols			All			Specific	-----------------------------------------	set_replace_col_status_for_ticker					--------------- 	replace_cols
# t-col		change col_adder		All			All			-----------------------------------------	set_replace_col_status_for_col_adder					---------------		replace_cols
# t-ALL 	replace all dfs	& cols	All			All			set_replace_df_status_for_all_tickers 		set_replace_cols_status_for_all_tickers 				replace_dfs			replace_cols
# Rdf		replace the DF			Specific	Specific	set_replace_df_status_for_ticker_and_page	------------------------------------------------	
# Rcol		replace the cols		Specific	Specific	-----------------------------------------	set_replace_col_adder_status_for_ticker_and_page









from audit import audit_replace_df_status
# audit_replace_df_status(scope)

# if 'initial_load' in scope:
# 	print(scope.config['charts'].keys())
# 	print('-'*50)
# 	print('Scope.Pages Templates - Charts')
# 	print(scope.pages['templates']['charts'])
# 	print('-'*50)

# print('widget_single_search = ', scope.widget_single_search)










# print('-'*75)
# print('Configurable chart variables')
# for chart in scope.config['charts']['chart_list']:
# 	active_status = scope.config['charts'][chart]['active']
# 	print(chart.upper(), '   -   active = ', active_status)
# 	add_columns = scope.config['charts'][chart]['add_columns']
# 	if add_columns != None:
# 		# print(add_columns)
# 		for attribute in add_columns.keys():
# 			if attribute not in ['function' ]:
# 				print(attribute)

# print('-'*75)
# print('Configurable test variables')
# for test in scope.config['tests']['test_list']:
# 	active_status = scope.config['tests'][test]['active']
# 	print(test.upper(), '   -   active = ', active_status)
# 	add_columns = scope.config['tests'][test]['add_columns']
# 	if add_columns != None:
# 		# print(add_columns)
# 		for attribute in add_columns.keys():
# 			if attribute not in ['function']:
# 				print(attribute)




	# print(scope.config['charts'][chart]['active'])





# ichi_moku_daily
# {'active': False, 'name': 'Icki Moku Daily', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdb896dc280>, 'colour': 'black'}, 'add_columns': None}







def terminal_heading(heading):
	print('')
	print('='*70)
	print(heading.upper(), '   ( level_1 )')
	print('='*70)


# def level_2_details(level_1, level_2):
# 	# print('')
# 	print('-'*40)
# 	print(level_1, '/', level_2, ' ( level 2 )', )
# 	print('-'*40)
# 	if level_2 in st.session_state[level_1]:
# 		for key in st.session_state[level_1][level_2]:
# 			print(level_2 , ' - ', key)

# def level_3_details(level_1, level_2, level_3):
# 	print('-'*50)
# 	print(level_1, '/', level_2, '/', level_3, ' ( level 3 )')
# 	print('-'*50)
# 	if level_2 in st.session_state[level_1]:
# 		if level_3 in st.session_state[level_1][level_2]:
# 			for key in st.session_state[level_1][level_2][level_3]:
# 				print(level_3 , ' - ', key)



# if 'initial_load' in st.session_state:
# 	print('')
# 	terminal_heading('All keys in st.session_state')
# 	for key in sorted(st.session_state):print(key)
	# for key in st.session_state:print(key)


# level_1 = 'config'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'dropdowns')
	# level_2_details(level_1, 'tests')
	# level_3_details(level_1, 'tests', 'trend_high')
# 	level_2_details(level_1, 'charts')
# 	level_3_details(level_1, 'charts', 'config')
# 	level_2_details(level_1, 'results')

# level_1 = 'files'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'folders')
# 	level_2_details(level_1, 'paths')

level_1 = 'data'
if level_1 in st.session_state:
	terminal_heading(level_1)
	for key in st.session_state[level_1]:print(key)
	level_2_details(level_1, 'ticker_files')
	level_2_details(level_1, 'tickers')
	# level_3_details(level_1, 'tickers', 'file')
	level_2_details(level_1, 'download')


print(scope.data['tickers'])





# level_1 = 'pages'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# # 	level_2_details(level_1, 'templates')
# 	level_2_details(level_1, 'single')
# 	level_2_details(level_1, 'intraday')
# 	level_2_details(level_1, 'volume')
# 	level_2_details(level_1, 'research')
# 	level_2_details(level_1, 'screener')
# 	level_3_details(level_1, 'single', 'renew')
# 	# level_3_details(level_1, 'single', 'chart')
	# level_3_details(level_1, 'screener', 'ticker_data')
	# level_3_details(level_1, 'screener', 'ticker_data')
	# level_3_details(level_1, 'screener', 'ticker_data')
	# level_3_details(level_1, 'screener', 'ticker_data')

	
	

# level_1 = 'strategy'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'header')
# 	level_2_details(level_1, 'print')

# print ( '='*70)
# print('screener/test_results')
# print(st.session_state['pages']['screener']['test_results'])


# print('data/download/yf_anomolies')
# print(st.session_state['data']['download']['yf_anomolies'])
# print ( '='*70)




# print( '^'*70)
# print('Report on Data Refresh State for each Object')
# print( '^'*70)

# for page in st.session_state['pages']['page_list']:
# 	print('='*100)	
# 	print('Page > ', page)
# 	print('='*100)	
# 	print( '-'*70)
# 	print('OHLCV refresh status')
# 	for key, value in st.session_state['pages'][page]['renew']['ticker_data'].items():
# 		print (key, ':', value)
# 	print( '-'*70)
# 	print('Charts refresh status')
# 	if page != 'screener':
# 		for key, value in st.session_state['pages'][page]['renew']['charts'].items():
# 			print (key, ':', value)
# 	print( '-'*70)
# 	print('Metrics refresh status')
# 	if page == 'screener':
# 		for key, value in st.session_state['pages'][page]['renew']['tests'].items():
# 			print (key, ':', value)

































# Happy 60th Big Fella
# You have aged well
# It must be all that red wine keeping you well preserved
# Enjoy the celebrations. 
# Party hard
# All the best, Rob and Fliss



