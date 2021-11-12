# streamlit run app.py
# -------------------------------------------------
# git push -u origin <branch>
# git branch -d <branch>   will delete local branch
# pipenv install flask==0.12.1

# pipenv install mplfinance===0.12.7a5
							# 0.12.7a17     


# TODO - remove un-needed libraries - ie TA maybe some other have been installed



import streamlit as st

project_description = 'DDT - Data Driven Trading'

from scope import set_streamlit_config, set_initial_scope, update_dropdown_lists
from navigation import set_page, render_current_page


# Set Up the Initial Streamlit Environment ======================================================================
set_streamlit_config()
set_initial_scope(st.session_state, project_description)

# Update the lists utilised by dropdown widgets 
#  (but only after loading or changing/refreshing the share index file)
if st.session_state.dropdown_lists_need_updating: 
	update_dropdown_lists(st.session_state)


# Temp Code to signal appl refresh ( delete later ) *************************************************************
print ( '='*80)
print ( 'A Refresh of the application has occured')
import sys
print(sys.version)
print ( '-'*80)
print ( '*'*80)
# ***************************************************************************************************************


# Display Appropriate Page ====================================================================================== 
render_current_page(st.session_state.display_page)


# Sidebar Action Buttons ======================================================================================= 
st.sidebar.title(project_description)
st.sidebar.button(('Ticker Index ( ' + str((len(st.session_state.ticker_index_file))) + ' )'), on_click=set_page, args=('ticker_index', ))
st.sidebar.button(('Ticker List  ( ' + str((len(st.session_state.ticker_list))) + ' )'), on_click=set_page, args=('ticker_list', ))
st.sidebar.button(('Ticker Files ( ' + str(len(st.session_state.share_data_files.keys())) + ' )'), on_click=set_page, args=('share_data_files', ))
st.sidebar.button('Scope', on_click=set_page, args=('scope', ))
# st.download_days = st.sidebar.number_input('change ( - / + )  number of days to download', min_value=1, max_value=6000, value=1, key='0')   

st.sidebar.title('Analysis')
# col1,col2 = st.sidebar.columns(2)

st.sidebar.button('Multiple'	, on_click=set_page, args=('analysis_multi', ))
st.sidebar.button('Single'  	, on_click=set_page, args=('single_analysis', ))
st.sidebar.button('Intra-Day'	, on_click=set_page, args=('intraday_analysis', ))
st.sidebar.button('Volume'		, on_click=set_page, args=('volume', ))
st.sidebar.button('Research'	, on_click=set_page, args=('research', ))


st.sidebar.title('Charts')
st.sidebar.checkbox('CandleStick', value=True)
st.sidebar.checkbox('Line')
st.sidebar.checkbox('MACD')
st.sidebar.checkbox('Stochastic')
st.sidebar.checkbox('?? Ichi Moku')
st.sidebar.checkbox('?? Heikin Ashi')
st.sidebar.checkbox('?? VAC')
st.sidebar.checkbox('?? Volume Oscillator')

st.sidebar.title('Additional')
st.sidebar.checkbox('add Bollinger Bands')
st.sidebar.checkbox('add Dividends')
st.sidebar.checkbox('add Announcements')

# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)




