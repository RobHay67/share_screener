# streamlit run app.py
# git push -u origin <branch>
# pipenv install flask==0.12.1

project_description = 'Share Trader - DDT'


# from scope import set_initial_scope, build_ticker_dropdowns, render_scope_page

from scope import set_initial_scope
from scope import build_ticker_dropdowns
from scope import render_scope_page
from share_index import render_share_index_page
from share_data import render_share_data_page, render_share_data_file
from company_profile import render_company_profile_page
from analysis import render_analysis_page
from ticker_list import construct_list_of_share_codes, render_ticker_list
from volume import render_volume_page

# Set Up Streamlit Environment ==================================================================================
import streamlit as st
st.set_page_config(layout="wide")
set_initial_scope(st.session_state, project_description)
# Update the dropdowns, but only on an initial build or after downloading new tickers from the ASX
if st.session_state.update_dropdown_lists: build_ticker_dropdowns(st.session_state)


# ===============================================================================================================
print ( '='*80)
print ( 'A Refresh of the application has occured')
import sys
print(sys.version)
print ( '-'*80)

print ( '*'*80)

# Display Appropriate Page ====================================================================================== 

# if   st.session_state.display_page == 'home': render_home_page(st.session_state)
  
if st.session_state.display_page == 'share_index': render_share_index_page(st.session_state)
elif st.session_state.display_page == 'ticker_list': render_ticker_list(st.session_state)
elif st.session_state.display_page == 'manage_share_data': render_share_data_page(st.session_state)
elif st.session_state.display_page == 'share_data_files': render_share_data_file(st.session_state)
elif st.session_state.display_page == 'volume':	render_volume_page(st.session_state)  
elif st.session_state.display_page == 'company_profile': render_company_profile_page(st.session_state)
elif st.session_state.display_page == 'analysis': render_analysis_page(st.session_state)
elif st.session_state.display_page == 'scope': render_scope_page(st.session_state)

# Call Backs for Sidebar Action Buttons ========================================================================= 
# def show_home_page(): st.session_state.display_page = 'home'
def page_share_index(): st.session_state.display_page = 'share_index'
def update_ticker_list_required(): st.session_state.update_ticker_list_required = True
def page_show_ticker_list(): st.session_state.display_page = 'ticker_list'
def page_manage_share_data(): st.session_state.display_page = 'manage_share_data'
def page_share_data_files(): st.session_state.display_page = 'share_data_files'
def page_volume(): st.session_state.display_page = 'volume'
def page_company_profile(): st.session_state.display_page = 'company_profile'
def page_analysis(): st.session_state.display_page = 'analysis'
def page_scope(): st.session_state.display_page = 'scope'

# Sidebar Action Buttons ======================================================================================= 
st.sidebar.title(project_description)
st.sidebar.button(('Share Index ( ' + str((len(st.session_state.share_index_file))) + ' )'), on_click=page_share_index)

# Select Tickers -----------------------------------------------------------------------------------------------
st.sidebar.subheader('Choose Tickers (lowest takes precedence)')
market   = st.sidebar.selectbox  ('Choose a Market'  	, st.session_state.dropdown_markets   , on_change=update_ticker_list_required, help='Select an Entire Share Market for Analysis')
industry = st.sidebar.multiselect('Choose Industries'	, st.session_state.dropdown_industries, on_change=update_ticker_list_required, help='Quickly Select all tickers in a particular industry')
tickers  = st.sidebar.multiselect('Choose Tickers'   	, st.session_state.dropdown_tickers   , on_change=update_ticker_list_required, help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list') 
ticker   = st.sidebar.selectbox  ('Choose a lone Ticker', st.session_state.dropdown_single_ticker   , on_change=update_ticker_list_required, help='Select a single ticker only. Start typing to jump within list') 

# Update the ticker list if required (selector box has changed)
if st.session_state.update_ticker_list_required:
	st.session_state.chosen_market = market
	st.session_state.chosen_industries = industry
	st.session_state.chosen_tickers = tickers
	st.session_state.chosen_single_ticker = ticker
	construct_list_of_share_codes(st.session_state)

# ticker list and ticker data buttons
st.sidebar.button( ('Show Ticker List ( ' + str((len(st.session_state.ticker_list))) + ' )'), on_click=page_show_ticker_list )
# st.sidebar.button( ('Load and Import Share Data'), on_click=page_manage_share_data)
st.sidebar.button( ('Load and Import Share Data ( ' + str((len(st.session_state.share_data_files))) + ' )'), on_click=page_manage_share_data )
# st.info(('Current number of Loaded Files ( ' + str((len(scope.share_data_files))) + ' )'))
st.sidebar.button( ('Show Share Data Files ( ' + str(len(st.session_state.share_data_files.keys())) + ' )'), on_click=page_share_data_files)

# Analysis Pages -----------------------------------------------------------------------------------------------
st.sidebar.subheader('Analysis')
# st.sidebar.info('Ticker List ( ' + str((len(st.session_state.ticker_list))) + ' )')
st.sidebar.button('Volume Analysis', on_click=page_volume)

st.sidebar.button('Company Profile', on_click=page_company_profile)
st.sidebar.button('Perform Analysis', on_click=page_analysis)


# System Variables ---------------------------------------------------------------------------------------------
st.sidebar.subheader('System Variables')
st.sidebar.button('Scope Variables', on_click=page_scope)











# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)