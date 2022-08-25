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



from scope import set_scope
from partials.sidebar import render_sidebar
from apps.routes import render_selected_app

print ( '\033[94m' + 'Application Re-Rendering Now ' + '>'*50 + '\033[0m')


scope = set_scope(st.session_state)

render_sidebar(scope)
render_selected_app(scope)


#TODO

# print('Render a progress bar')
# import time

# my_bar = st.progress(0)

# my_bar.progress(6+1)
# my_bar.progress(12+1)
# my_bar.progress(20+1)
# my_bar.progress(40+1)
# my_bar.progress(99+1)

# for percent_complete in range(100):
#      time.sleep(0.1)
#      my_bar.progress(percent_complete + 1)

# Assume 6 items

# for ticker in range(1,100, 6):
# 	print(ticker)
# 	my_bar.progress(ticker+1)







# print('Missing Tickers - local  = ', scope.missing_tickers['local'])
# print('Missing Tickers - cloud  = ', scope.missing_tickers['cloud'])
# print('Missing Tickers - list   = ', scope.missing_tickers['list'])
# print('Missing Tickers - Errors = ', scope.missing_tickers['errors'])



# print('='*88)
# print('Download Parameters')
# print('-'*88)
# print('scope.download[yf_download_these_industries] > ', scope.download['yf_download_these_industries'])
# print('scope.download[yf_batch_ticker_string]   > ', scope.download['yf_batch_ticker_string'])
# print('scope.download[yf_batch_type]          > ', scope.download['yf_batch_type'])
# print('scope.download[yf_errors]          > ', scope.download['yf_errors'])
# print('='*88)


# print('='*88)
# print('Screener App')
# print('-'*88)
# # print('search results   (screener) = ', scope.apps['screener']['search_results'])
# print('Ticker Worklist  (screener) = ', scope.apps['screener']['worklist'])
# print('mined_ticker     (screener) = ', scope.apps['screener']['mined_tickers'])
# print('='*88)



# print('IntraDay search results = ', scope.apps['intraday']['search_results'])
# print('Single search results   = ', scope.apps['single']['search_results'])
# print('Research search results = ', scope.apps['research']['search_results'])
# print('Screener search results = ', scope.apps['screener']['search_results'])



# st.info('Info')
# st.error('error')
# st.warning('warning')
# st.success('Success')
# st.exception('exception')




# =======================================
# Testing code - show whats in scope

def terminal_heading(heading):
	print('')
	print('='*70)
	print(heading.upper(), '   ( level_1 )')
	print('='*70)


def level_2_details(level_1, level_2):
	# print('')
	print('-'*40)
	print(level_1, '/', level_2, ' ( level 2 )', )
	print('-'*40)
	if level_2 in st.session_state[level_1]:
		for key in st.session_state[level_1][level_2]:
			print(level_2 , ' - ', key)

def level_3_details(level_1, level_2, level_3):
	print('-'*50)
	print(level_1, '/', level_2, '/', level_3, ' ( level 3 )')
	print('-'*50)
	if level_2 in st.session_state[level_1]:
		if level_3 in st.session_state[level_1][level_2]:
			# print(st.session_state[level_1][level_2])
			for key in st.session_state[level_1][level_2][level_3]:
				print(level_3 , ' - ', key)
				# print(type(st.session_state[level_1][level_2][level_3]))


# if 'initial_load' in st.session_state:
# 	print('')
# 	terminal_heading('All keys in st.session_state')
# 	for key in sorted(st.session_state):print(key)



# ==============================================================================================
# Structure for the tickers scope object
# ==============================================================================================

# level_1 = 'tickers'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)

# 	temp_scope = st.session_state[level_1]

# 	for ticker in temp_scope:
# 		print('='*99)
# 		print('\033[93m', ticker, '\033[0m')
# 		print('Loaded df = ', len(temp_scope[ticker]['df']))
# 		print('-'*99)
# 		for app in temp_scope[ticker]['apps']:
# 			print ('\033[96m', app.upper(), '\033[0m')
# 			print('-'*99)
# 			print('Dataframe size'.ljust(20), ' = ', len(temp_scope[ticker]['apps'][app]['df']))
# 			print('-'*99)
# 			print('Replace App DF'.ljust(20), ' = ', temp_scope[ticker]['apps'][app]['replace_df'])
# 			print('-'*99)
# 			type_col_adder = temp_scope[ticker]['apps'][app]['type_col_adder']
# 			print('Type of Column Adder'.ljust(20), ' = ', type_col_adder)
# 			if type_col_adder != None:
# 				print('-'*99)
# 				for column_adder, status in temp_scope[ticker]['apps'][app]['column_adders'].items():
# 					print(str(column_adder).ljust(20),  ' : ', status)
# 			print('-'*99)


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

	
	

# level_1 = 'apps'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'single')

# print('='*88)
# print('Screener App')
# print('-'*88)
# # print('trial list       (trials)   = ', scope.trial_config['trial_list'])
# # print('column adders    (trials)   = ', scope.trial_config['column_adders'])
# # print('active list      (trials)   = ', scope.trial_config['active_list'])
# print('-'*88)
# print('search results   (screener) = ', scope.apps['screener']['search_results'])
# print('selected tickers (screener) = ', scope.apps['screener']['worklist'])
# print('mined_ticker     (screener) = ', scope.apps['screener']['mined_tickers'])
# print('='*88)


# print('='*88)
# print('Single App')
# print('-'*88)
# # print('trial list       (charts) = ', scope.chart_config['chart_list'])
# # print('column adders    (charts) = ', scope.chart_config['column_adders'])
# # print('active list      (charts) = ', scope.chart_config['active_list'])
# print('-'*88)
# print('search results   (single) = ', scope.apps['single']['search_results'])
# print('selected tickers (single) = ', scope.apps['single']['worklist'])
# print('mined_ticker     (single) = ', scope.apps['single']['mined_tickers'])
# print('='*88)


# level_1 = 'trials'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'column_adders')
# 	level_2_details(level_1, 'trend_open')


# level_1 = 'charts'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'column_adders')
# 	level_2_details(level_1, 'trend_open')

# level_1 = 'chart_config'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'column_adders')
# 	level_2_details(level_1, 'trend_open')


# level_1 = 'trial_config'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'column_adders')
# 	level_2_details(level_1, 'trend_open')



# print('-'*75)
# print('Configurable chart variables')
# for chart in scope.chart_config['chart_list']:
# 	active_status = scope.charts[chart]['active']
# 	print(chart.upper(), '   -   active = ', active_status)
# 	add_columns = scope.charts[chart]['add_columns']
# 	if add_columns != None:
# 		# print(add_columns)
# 		for attribute in add_columns.keys():
# 			if attribute not in ['function' ]:
# 				print(attribute)

# print('-'*75)
# print('Configurable trial variables')
# for trial in scope.trials['test_list']:
# 	active_status = scope.trials[trial]['active']
# 	print(trial.upper(), '   -   active = ', active_status)
# 	add_columns = scope.trials[trial]['add_columns']
# 	if add_columns != None:
# 		# print(add_columns)
# 		for attribute in add_columns.keys():
# 			if attribute not in ['function']:
# 				print(attribute)




















# Happy 60th Big Fella
# You have aged well
# It must be all that red wine keeping you well preserved
# Enjoy the celebrations. 
# Party hard
# All the best, Rob and Fliss



