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

# Testing Code - TODO - delete on Final Release
from tokenize import Single
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


from audit import audit_replace_df_status


import streamlit as st

from config.controller import set_scope
from pages.sidebar.sidebar import render_sidebar
from pages.controller import render_selected_page

print ( '\033[94m' + 'Application Re-Rendering Now ' + '>'*50 + '\033[0m')


scope = set_scope(st.session_state)
render_sidebar(scope)
render_selected_page(scope)




# audit_replace_df_status(scope)



# we need to ensure that the user has a setting for each of the charts and tests
# we want to be able to upodate the user settings
# we want to save the settings


# x load default config
# wip load user config
# replace default with user config
# we can then add new config and it will automatically get added when we save user config
# Save User config

#


















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



# [pipenv.exceptions.InstallError]: hint: See above for details.
# ERROR: Couldn't install package: pathlib
#  Package installation failed...
# /app/share_screener
# [manager] installer returned a non-zero exit code
# [manager] Error during processing dependencies! Please fix the error and push an update, or try restarting the app.
# [manager] Streamlit server consistently failed status checks
# [manager] Please fix the errors, push an update to the git repo, or reboot the app.
# [manager] Pulling code changes from Github...
# [manager] Processing dependencies...
# /app/share_screener /app/share_screener
# Installing dependencies from Pipfile.lock (c2396e)...
# Ignoring appnope: markers 'sys_platform == "darwin" and platform_system == "Darwin"' don't match your environment
# To activate this project's virtualenv, run pipenv shell.
# Alternatively, run a command inside the virtualenv with pipenv run.
# /app/share_screener
# [manager] Python dependencies were installed from /app/share_screener/Pipfile using pipenv.
# [manager] Processed dependencies!
# 2022-04-25 23:19:16.981 INFO    matplotlib.font_manager: generated new fontManager
# [manager] Updated app!

























# Happy 60th Big Fella
# You have aged well
# It must be all that red wine keeping you well preserved
# Enjoy the celebrations. 
# Party hard
# All the best, Rob and Fliss



