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

import jupyter_client
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






print('Rob we are working on the new structure for the scope.tickers')
print('See notes in tickers.status.notes.py')









# from audit import audit_replace_df_status
# audit_replace_df_status(scope)

# if 'initial_load' in scope:
# 	print(scope.charts.keys())
# 	print('-'*50)
# 	print('scope.apps Templates - Charts')
# 	print(scope.apps['templates']['charts'])
# 	print('-'*50)

# print('widget_single_search = ', scope.widget_single_search)










# print('-'*75)
# print('Configurable chart variables')
# for chart in scope.charts['chart_list']:
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




	# print(scope.charts[chart]['active'])





# ichi_moku_daily
# {'active': False, 'name': 'Icki Moku Daily', 'is_overlay': True, 'add_overlays': False, 'plot': {'function': <function sma_plot at 0x7fdb896dc280>, 'colour': 'black'}, 'add_columns': None}







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
# 	for key in st.session_state:print(key)



# level_1 = 'apps'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'screener')
# 	level_2_details(level_1, 'single')
# 	# level_3_details(level_1, 'trials', 'trend_high')
# 	# level_2_details(level_1, 'charts')
# 	level_3_details(level_1, 'single', 'search_results')
	# level_3_details(level_1, 'screener', 'ticker_list')
	# level_2_details(level_1, 'results')

# level_1 = 'trials'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'trends')
# 	level_2_details(level_1, 'trial_list')
# 	level_2_details(level_1, 'trend_open')


# ==============================================================================================
# Structure for the tickers scope object
# ==============================================================================================

level_1 = 'tickers'
if level_1 in st.session_state:
	terminal_heading(level_1)

	temp_scope = st.session_state[level_1]

	for ticker in temp_scope:
		print('='*99)
		print(ticker)
		print('-'*99)
		print('replace_app_dfs'.ljust(20), ' = ', temp_scope[ticker]['replace_app_dfs'])
		print('-'*99)
		# print(temp_scope[ticker]['apps'])
		for app in temp_scope[ticker]['apps']:
			print ('\033[96m', app.upper(), '\033[0m')
			print('-'*99)
			for object in temp_scope[ticker]['apps'][app].keys():
				if object == 'df':
					print('Dataframe size'.ljust(20), ' = ', len(temp_scope[ticker]['apps'][app]['df']))
					print('-'*99)
				else:
					print(str(object).ljust(20),  ' : ', temp_scope[ticker]['apps'][app][object])
			print('-'*99)




	# level_2_details(level_1, 'ticker_files')
	# level_2_details(level_1, 'tickers')
	# # level_3_details(level_1, 'tickers', 'file')
	# level_2_details(level_1, 'download')





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
# print('screener/trial_results')
# print(st.session_state['pages']['screener']['trial_results'])


# print('data/download/yf_anomolies')
# print(st.session_state['data']['download']['yf_anomolies'])
# print ( '='*70)




# print( '^'*70)
# print('Report on Data Refresh State for each Object')
# print( '^'*70)

# for app in st.session_state['pages']['app_list']:
# 	print('='*100)	
# 	print('app > ', app)
# 	print('='*100)	
# 	print( '-'*70)
# 	print('OHLCV refresh status')
# 	for key, value in st.session_state['pages'][app]['renew']['ticker_data'].items():
# 		print (key, ':', value)
# 	print( '-'*70)
# 	print('Charts refresh status')
# 	if app != 'screener':
# 		for key, value in st.session_state['pages'][app]['renew']['charts'].items():
# 			print (key, ':', value)
# 	print( '-'*70)
# 	print('Metrics refresh status')
# 	if app == 'screener':
# 		for key, value in st.session_state['pages'][app]['renew']['trials'].items():
# 			print (key, ':', value)







# Apps Object 10:17 on 31 July
# {
# 	'row_limit': 100.0, 
# 	'button_for_scope': None, 
# 	'display_app': 'home_page', 
# 	'page_list': ['single', 'intraday', 'volume', 'research', 'screener'], 
# 	'templates': {
# 		'trials': {'trend_open': False, 'trend_high': True, 'trend_low': False, 'trend_close': True, 'trend_volume': False}, 
# 		'charts': {'macd': True, 'macd_vol': True, 'rsi': True, 'vol_osssy': False, 'stochastic': True, 'sma_1': True, 'sma_2': False, 'sma_3': False, 'ema_1': False, 'ema_2': False, 'ema_3': False, 'bollinger_bands': False, 'dividends': True, 'candlestick': True, 'scatter': False, 'bar': False, 'line': True, 'heiken_ashi': False, 'volume': True, 'vol_per_minute': False, 'vac': False, 'announcements': False, 'ichi_moku': False, 'ichi_moku_daily': False}}, 
# 	'single': {
# 		'search_results': {}, 
# 		'ticker_list': [], 
# 		'replace_dfs': {}, 
# 		'replace_cols': {}, 
# 		'dfs': {}, 
# 		'data': {}, 
# 		'selectors': {'market': 'select entire market', 'industries': [], 'tickers': [], 'ticker': 'select a ticker'}
# 			}, 
# 	'intraday': {
# 		'search_results': {}, 
# 		'ticker_list': [], 
# 		'replace_dfs': {}, 
# 		'replace_cols': {}, 
# 		'dfs': {}, 
# 		'data': {}, 
# 		'selectors': {'market': 'select entire market', 'industries': [], 'tickers': [], 'ticker': 'select a ticker'}
# 		}, 
# 	'volume': {
# 		'search_results': {}, 
# 		'ticker_list': [], 
# 		'replace_dfs': {}, 
# 		'replace_cols': {}, 
# 		'dfs': {}, 
# 		'data': {}, 
# 		'selectors': {'market': 'select entire market', 'industries': [], 'tickers': [], 'ticker': 'select a ticker'}
# 		}, 
# 	'research': {
# 		'search_results': {}, 
# 		'ticker_list': [], 
# 		'replace_dfs': {}, 
# 		'replace_cols': {}, 
# 		'dfs': {}, 
# 		'data': {}, 
# 		'selectors': {'market': 'select entire market', 'industries': [], 'tickers': [], 'ticker': 'select a ticker'}
# 		}, 
# 	'screener': {
# 		'search_results': {}, 
# 		'ticker_list': [], 
# 		'replace_dfs': {}, 
# 		'replace_cols': {}, 
# 		'dfs': {}, 
# 		'data': {}, 
# 		'selectors': {'market': 'select entire market', 'industries': [], 'tickers': [], 'ticker': 'select a ticker'}
# 		}, 
# 	'trials': {'results': {}, 'df': {}}
# }



















# Happy 60th Big Fella
# You have aged well
# It must be all that red wine keeping you well preserved
# Enjoy the celebrations. 
# Party hard
# All the best, Rob and Fliss



