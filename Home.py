# ------------------------------------------------- Execute Application
# pipenv shell
# streamlit run home.py
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
# upgrade package	- pipenv update yfinance (but wont override version specified in pipfile)
# specify ver   	- pipenv install mplfinance==0.12.7a5
# latest ver		- pipenv update pandas
# delete pkg		- pipenv uninstall django
# -------------------------------------------------

for i in range(10):print('')
print ( '\033[94m' + 'Application Re-Rendering - see below this line ' + '>'*50 + '\033[0m')
for i in range(5):print('')

import streamlit as st
from scope import set_scope
from pages.sidebar.sidebar import render_sidebar
from pages.users.login import render_login_page
from pages.header.page_title import page_title_layer


if 'display_page' not in st.session_state:
	scope = set_scope(st.session_state)


# Page Configuration
scope = st.session_state
page = 'home'
page_title = scope.config['project_description']
page_icon = '🏠'
# -----------------------------
scope.display_page = page


# print(page, ' > Number of Keys in Scope = ', len(scope))
# for count, key in enumerate(sorted(st.session_state)):print(count+1, key)

page_title_layer(scope, page_title, page_icon)
st.write('Welcome to the Share Picker Appliction.')
st.write('Select from the options in the sidebar (left)')
st.warning('Users Logged in = ' + str(scope.user_logged_in))

if scope.user_logged_in == False:
	col1,col2 = st.columns([2,8])
	with col1:render_login_page(scope)
else:
	render_sidebar(scope)



#======================================================== TODO s
print('='*66)
print('TODOs - list every thing I think of while coding')
print('move this to Trello as soon as you can')
print('-'*66)
print('TODO - we need to download and SAVE the dividend data as well')
print('TODO - might need some code to detect multiple sessions open')
print('='*66)


# if 'initial_load' in st.session_state:
# 	for key in sorted(st.session_state):print(key)


# =======================================
# Testing code - show whats in scope
# =======================================



# def terminal_heading(heading):
# 	print('')
# 	print('='*70)
# 	print(heading.upper(), '   ( level_1 )')
# 	print('='*70)


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
# 			# print(st.session_state[level_1][level_2])
# 			for key in st.session_state[level_1][level_2][level_3]:
# 				print(level_3 , ' - ', key)
# 				# print(type(st.session_state[level_1][level_2][level_3]))


# if 'initial_load' in st.session_state:
# 	print('')
# 	terminal_heading('All keys in st.session_state')
# 	for key in sorted(st.session_state):print(key)


# if 'initial_load' in st.session_state:
# 	scope = st.session_state
# 	# scope.users['user_list'] = [rob, Fliss]
# 	# json file has structure
# 	for key in sorted(scope.users):print(key)
# 	# for key in sorted(scope.users['json']['Rob']):print(key)


