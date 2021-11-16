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
from system.scope import set_scope
from system.dropdowns import update_dropdowns
from system.navigation import set_page, view_current_page
# from system.chart import chart_change

# Set Up the Initial Streamlit Environment ======================================================================
set_streamlit_config()
set_scope(st.session_state, project_description)

# Update the lists utilised by dropdown widgets 
#  (but only after loading or changing/refreshing the share index file)
if st.session_state.dropdown_lists_need_updating: 
	update_dropdowns(st.session_state)


print ( '\033[94mApplication Refreshed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \033[0m')


# Display Appropriate Page
view_current_page(st.session_state.display_page)

# Sidebar Action Buttons
st.sidebar.title(project_description)
st.sidebar.button('Charting', on_click=set_page, args=('charts', ))
st.sidebar.button('Defaults', on_click=set_page, args=('user', ))

st.sidebar.title('Analysis')
st.sidebar.button('Single'  	, on_click=set_page, args=('single', ))
st.sidebar.button('Intra-Day'	, on_click=set_page, args=('intraday', ))
st.sidebar.button('Volume'		, on_click=set_page, args=('volume', ))
st.sidebar.button('Research'	, on_click=set_page, args=('research', ))
st.sidebar.button('Multiple'	, on_click=set_page, args=('multi', ))

st.sidebar.title('System Settings')
st.sidebar.button('Settings', on_click=set_page, args=('scope', ))



# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)




