# streamlit run app.py
# git push -u origin <branch>
# pipenv install flask==0.12.1



project_description = 'Share Trader - DDT'


from scope import set_initial_scope
from scope import update_lists_for_dropdowns
from navigation import render_current_page, set_page


# Set Up Streamlit Environment ==================================================================================
import streamlit as st
st.set_page_config(layout="wide")
set_initial_scope(st.session_state, project_description)

# Update the lists utilised by dropdown widgets (but only after loading or changing the share index file)
if st.session_state.update_lists_for_dropdowns: 
	update_lists_for_dropdowns(st.session_state)


# Temp Code to signal appl refresh ( delete later ) =============================================================
print ( '='*80)
print ( 'A Refresh of the application has occured')
import sys
print(sys.version)
print ( '-'*80)
print ( '*'*80)

# Display Appropriate Page ====================================================================================== 
render_current_page(st.session_state.display_page)


# Sidebar Action Buttons ======================================================================================= 
st.sidebar.title(project_description)
st.sidebar.button(('Ticker Index ( ' + str((len(st.session_state.ticker_index_file))) + ' )'), on_click=set_page, args=('ticker_index', ))
st.sidebar.button(('Ticker List  ( ' + str((len(st.session_state.ticker_list))) + ' )'), on_click=set_page, args=('ticker_list', ))
st.sidebar.button(('Ticker Files ( ' + str(len(st.session_state.share_data_files.keys())) + ' )'), on_click=set_page, args=('share_data_files', ))

st.download_days = st.sidebar.number_input('change ( - / + )  number of days to download', min_value=1, max_value=6000, value=1, key='0')   

st.sidebar.title('Analysis ( multiple tickers )')
st.sidebar.button('Ticker Analysis (multiple)', on_click=set_page, args=('analysis_multi', ))
st.sidebar.button('Ticker Analysis (single)'  , on_click=set_page, args=('single_analysis', ))
st.sidebar.button('Company Profile'	 , on_click=set_page, args=('company_profile', ))
st.sidebar.button('Volume Prediction', on_click=set_page, args=('volume', ))
st.sidebar.button('Intra-Day Analysis'	 , on_click=set_page, args=('intraday_analysis', ))


st.sidebar.title('Variables')
st.sidebar.button('Session Variables', on_click=set_page, args=('scope', ))




# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)