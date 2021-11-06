# streamlit run app.py
# git push -u origin <branch>
# pipenv install flask==0.12.1



project_description = 'Share Trader - DDT'


from scope import set_initial_scope
from scope import refresh_ticker_dropdown_lists
from web_browser import render_current_page, set_page
# from share_data import construct_list_of_share_codes


# Set Up Streamlit Environment ==================================================================================
import streamlit as st
st.set_page_config(layout="wide")
set_initial_scope(st.session_state, project_description)
# Update the dropdowns, but only on an initial build or after downloading new tickers from the ASX
if st.session_state.update_dropdown_lists: 
	refresh_ticker_dropdown_lists(st.session_state)


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
st.sidebar.button(('Share Index ( ' + str((len(st.session_state.ticker_index_file))) + ' )'), on_click=set_page, args=('ticker_index', ))

st.sidebar.title('Analysis ( multiple tickers )')
st.sidebar.button('Multi Ticker Analysis', on_click=set_page, args=('multi_analysis', ))
st.sidebar.button( ('Load and Import Share Data ( ' + str((len(st.session_state.share_data_files))) + ' )'), on_click=set_page, args=('manage_share_data', ))

st.sidebar.title('Analysis ( single ticker )')
st.sidebar.button('Company Profile'	 , on_click=set_page, args=('company_profile', ))
st.sidebar.button('Volume Prediction', on_click=set_page, args=('volume', ))
st.sidebar.button('Daily Analysis'	 , on_click=set_page, args=('daily_analysis', ))

st.sidebar.title('Quick Data ( Temp )')
# ticker list and ticker data buttons
st.sidebar.button( ('Show Ticker List ( ' + str((len(st.session_state.tickers_for_multi))) + ' )'), on_click=set_page, args=('ticker_list', ))
st.sidebar.button( ('Show Share Data Files ( ' + str(len(st.session_state.share_data_files.keys())) + ' )'), on_click=set_page, args=('share_data_files', ))

st.sidebar.title('Variables')
st.download_days = st.sidebar.number_input('change ( - / + )  number of days to download', min_value=1, max_value=1000, value=1, key='0')   
st.sidebar.button('Session Variables', on_click=set_page, args=('scope', ))




# Select Tickers -----------------------------------------------------------------------------------------------
# def update_ticker_list_required(): st.session_state.update_ticker_list_required = True
# st.sidebar.subheader('Choose Tickers (lowest takes precedence)')
# market   = st.sidebar.selectbox  ('Choose a Market'  	, st.session_state.dropdown_markets   , on_change=update_ticker_list_required, help='Select an Entire Share Market for Analysis')
# industry = st.sidebar.multiselect('Choose Industries'	, st.session_state.dropdown_industries, on_change=update_ticker_list_required, help='Quickly Select all tickers in a particular industry')
# tickers  = st.sidebar.multiselect('Choose Tickers'   	, st.session_state.dropdown_tickers   , on_change=update_ticker_list_required, help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list') 
# ticker   = st.sidebar.selectbox  ('Choose a lone Ticker', st.session_state.dropdown_single_ticker   , on_change=update_ticker_list_required, help='Select a single ticker only. Start typing to jump within list') 

# Update the ticker list if required (selector box has changed)
# if st.session_state.update_ticker_list_required:
# 	st.session_state.chosen_market = market
# 	st.session_state.tickers_industries = industry
# 	st.session_state.tickers_tickers = tickers
#	st.session_state.chosen_single_ticker = ticker
# 	construct_list_of_share_codes(st.session_state)






# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)