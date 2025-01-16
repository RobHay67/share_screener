# ------------------------------------------------- Execute Application
# pipenv shell
# streamlit run streamlit_app.py
# ------------------------------------------------- 


import streamlit as st
from app.helpers.re_render import app_is_re_rendering
from app.scope.model.set_scope import set_scope
from users.views.login.controller import render_login_page
from app.views.sidebar.controller import render_sidebar

app_is_re_rendering()

if 'display_page' not in st.session_state:
	scope = set_scope(st.session_state)

# Page Setup
page = scope.config['page']
screener_page 	= st.Page(page=page['screener']['path'],	title=page['screener']['title'], 	icon=page['screener']['icon'], 		default=page['screener']['default'])
charting_page 	= st.Page(page=page['chart']['path'],		title=page['chart']['title'], 		icon=page['chart']['icon'], 		default=page['chart']['default'])
intra_day_page 	= st.Page(page=page['intraday']['path'],	title=page['intraday']['title'], 	icon=page['intraday']['icon'], 		default=page['intraday']['default'])
volume_page 	= st.Page(page=page['volume']['path'],		title=page['volume']['title'], 		icon=page['volume']['icon'], 		default=page['volume']['default'])
research_page 	= st.Page(page=page['research']['path'],	title=page['research']['title'], 	icon=page['research']['icon'], 		default=page['research']['default'])
websites_page 	= st.Page(page=page['websites']['path'],	title=page['websites']['title'], 	icon=page['websites']['icon'], 		default=page['websites']['default'])
ticker_idx_page = st.Page(page=page['ticker_index']['path'],title=page['ticker_index']['title'],icon=page['ticker_index']['icon'], 	default=page['ticker_index']['default'])
logout_page 	= st.Page(page=page['logout']['path'],		title=page['logout']['title'], 		icon=page['logout']['icon'], 		default=page['logout']['default'])
config_page 	= st.Page(page=page['config']['path'],		title=page['config']['title'], 		icon=page['config']['icon'], 		default=page['config']['default'])
testing_page 	= st.Page(page=page['testing']['path'],		title=page['testing']['title'], 	icon=page['testing']['icon'], 		default=page['testing']['default'])


page_navigation = st.navigation(
	{
		"Research & Analysis"	: [screener_page, charting_page, intra_day_page, volume_page, research_page, websites_page],
		"Config"	: [ticker_idx_page, config_page, logout_page, testing_page],
	}
)

# Render Pages
if scope.users['logged_in'] == True:
	page_navigation.run()		# Run Navigation
	render_sidebar(scope)	
else:
	render_login_page(scope)



#======================================================== TODO s
for i in range(5):print('')
print('='*66)
print('TODOs - document while coding then move to Trello')
print('TODO - we need to download and SAVE the dividend data as well')

print('='*66)
for i in range(3):print('')

print('='*66)
print('Total Keys in Scope = ', len(scope))
for count, key in enumerate(sorted(st.session_state)):print(count+1, key)
print('='*66)


# for key, item in scope.trials.items():
# 	print( key, '   :    ', item)














# =======================================
# Testing code - show whats in scope
# =======================================



# def terminal_heading(heading):
# 	print('')
# 	print('='*70)
# 	print(heading.upper(), '   ( level_1 )')
# 	print('='*70)


def level_2_details(level_1, level_2):
	# print('')
	print('-'*40)
	print(level_1, '/', level_2, ' ( level 2 )', )
	print('-'*40)
	if level_2 in st.session_state[level_1]:
		for key in st.session_state[level_1][level_2]:
			print(level_2 , ' - ', key)

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



# [packages]
# pandas = "==1.5.3"
# streamlit = "*"
# datetime = "*"
# yfinance = "==0.2.14"
# mplfinance = "===0.12.7a5"
# matplotlib = "*"
# plotly = "*"
# pytz = "==2023.3"
# watchdog = "*"
# streamlit-extras = "*"
# jinja2 = "*"

# [dev-packages]

# [requires]
# python_version = "3.8"