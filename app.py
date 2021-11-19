# streamlit run app.py
# -------------------------------------------------
# git push -u origin <branch>
# git branch -d <branch>   will delete local branch
# pipenv install flask==0.12.1

# pipenv install mplfinance===0.12.7a5
							# 0.12.7a17     


import streamlit as st

project_description = 'DDT - Data Driven Trading'

from config.streamlit import set_streamlit_config
from scope.scope import set_scope
from scope.dropdowns.refresh_selectors import update_dropdowns
from navigation.controller import view_selected_page, store_page

# Set Up the Initial Streamlit Environment ======================================================================
set_streamlit_config()
scope = set_scope(st.session_state, project_description)

if scope.dropdown_lists_need_updating: 
	update_dropdowns(scope)

print ( '\033[94mApplication Refreshed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \033[0m')

view_selected_page(scope.display_page)

# Sidebar Action Buttons
st.sidebar.title(project_description)
st.sidebar.subheader('Charts')
st.sidebar.button('Primary'		, on_click=store_page, args=('charts_primary', ))
st.sidebar.button('Secondary'	, on_click=store_page, args=('charts_secondary', ))
st.sidebar.button('Defaults'	, on_click=store_page, args=('user', ))

st.sidebar.subheader('Analysis')
st.sidebar.button('Single'  	, on_click=store_page, args=('single', ))
st.sidebar.button('Intra-Day'	, on_click=store_page, args=('intraday', ))
st.sidebar.button('Volume'		, on_click=store_page, args=('volume', ))
st.sidebar.button('Research'	, on_click=store_page, args=('research', ))
st.sidebar.button('Multiple'	, on_click=store_page, args=('multi', ))

st.sidebar.subheader('System Settings')
st.sidebar.button('Settings', on_click=store_page, args=('scope', ))



# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)




