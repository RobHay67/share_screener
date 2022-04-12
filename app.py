# ------------------------------------------------- Execute Application
# streamlit run app.py
# ------------------------------------------------- GitHub
# git push -u origin <branch>
# git branch -d <branch>   will delete local branch
# ------------------------------------------------- Package Management
# pip3 install --user --upgrade django
# pipenv install flask==0.12.1
# pipenv install mplfinance===0.12.7a5
# ------------------------------------------------- 

# Testing Code - TODO - delete later
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


from audit import audit_report


import streamlit as st

from config.controller import set_scope
from pages.sidebar.sidebar import render_sidebar
from pages.controller import render_selected_page

print ( '\033[94m' + 'Application Re-Rendering Now ' + '>'*50 + '\033[0m')


scope = set_scope(st.session_state)
audit_report(scope)
render_sidebar(scope)
render_selected_page(scope)



# for ticker in scope.pages['single']['df'].keys():
# 	print(ticker)
# 	print(scope.pages['single']['df'][ticker].sample(3))















# Happy 60th Big Fella
# You have aged well
# It must be all that red wine keeping you well preserved
# Enjoy the celebrations. 
# Party hard
# All the best, Rob and Fliss









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
			for key in st.session_state[level_1][level_2][level_3]:
				print(level_3 , ' - ', key)



# if 'initial_load' in st.session_state:
# 	print('')
# 	terminal_heading('All keys in st.session_state')
# 	for key in sorted(st.session_state):print(key)
# 	# for key in st.session_state:print(key)


# level_1 = 'config'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
	# for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'dropdowns')
	# level_2_details(level_1, 'tests')
	# level_3_details(level_1, 'tests', 'trend_open')
# 	level_2_details(level_1, 'charts')
# 	level_3_details(level_1, 'charts', 'config')
# 	level_2_details(level_1, 'results')

# level_1 = 'files'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'folders')
# 	level_2_details(level_1, 'paths')

# level_1 = 'data'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# 	level_2_details(level_1, 'download')
\
# level_1 = 'pages'
# if level_1 in st.session_state:
# 	terminal_heading(level_1)
# 	for key in st.session_state[level_1]:print(key)
# # 	level_2_details(level_1, 'templates')
# 	level_2_details(level_1, 'single')
# # 	level_2_details(level_1, 'intraday')
# # 	level_2_details(level_1, 'volume')
# # 	level_2_details(level_1, 'research')
# # 	level_2_details(level_1, 'screener')
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




