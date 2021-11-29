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




import streamlit as st

from config.controller import set_scope
from pages.view.sidebar import render_sidebar
from pages.controller import render_selected_page

print ( '\033[94m' + 'Application Re-Rendering Now ' + '>'*50 + '\033[0m')
scope = set_scope(st.session_state)
render_sidebar(scope)						# Render the Sidebar
render_selected_page(scope)				# Render the selected Page
















# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)














# # Set Up the Initial Streamlit Environment ======================================================================
# from config.streamlit import set_streamlit_page_config
# from scope.scope import set_scope
# from pages.controller import set_initial_scope
# from scope.dropdowns.refresh_selectors import update_dropdowns


# set_streamlit_page_config()
# scope = set_scope(st.session_state, project_description)

# if scope.dropdown_lists_need_updating: 
# 	update_dropdowns(scope)

# print ( '\033[94mApplication Refreshed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \033[0m')

# render_selected_page(scope)
# render_sidebar(scope)


