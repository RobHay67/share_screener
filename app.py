# streamlit run app.py

project_description = 'Share Trader - DDT'


# from scope import set_initial_scope, build_ticker_dropdowns, render_scope_page

from scope import set_initial_scope
from scope import build_ticker_dropdowns
from scope import render_scope_page
from share_index import load_share_index_file, render_share_index_page
from share_data import render_share_data_page, render_ticker_list, render_share_data_file
from ticker_list import construct_list_of_share_codes
from volume import render_volume_page

# Set Up Streamlit Environment ==================================================================================
import streamlit as st
st.set_page_config(layout="wide")
set_initial_scope(st.session_state, project_description)
# Update the dropdowns, but only on an initial build or after downloading new tickers from the ASX
if st.session_state.update_available_dropdowns: build_ticker_dropdowns(st.session_state)


# ===============================================================================================================
print ( '='*80)
print ( 'A Refresh of the application has occured')
import sys
print(sys.version)
print ( '-'*80)

print ( '*'*80)

# Display Appropriate Page ====================================================================================== 

# if   st.session_state.display_page == 'home': render_home_page(st.session_state)
if st.session_state.display_page == 'volume':	render_volume_page(st.session_state)    
elif st.session_state.display_page == 'share_index': render_share_index_page(st.session_state)
elif st.session_state.display_page == 'ticker_list': render_ticker_list(st.session_state)
elif st.session_state.display_page == 'manage_share_data': render_share_data_page(st.session_state)
elif st.session_state.display_page == 'share_data_files': render_share_data_file(st.session_state)
elif st.session_state.display_page == 'analysis': st.title('Analysis')
elif st.session_state.display_page == 'scope': render_scope_page(st.session_state)

# Call Backs for Sidebar Action Buttons ========================================================================= 
# def show_home_page(): st.session_state.display_page = 'home'
def page_share_index(): st.session_state.display_page = 'share_index'
def update_ticker_list_required(): st.session_state.update_ticker_list_required = True
def page_show_ticker_list(): st.session_state.display_page = 'ticker_list'
def page_manage_share_data(): st.session_state.display_page = 'manage_share_data'
def page_share_data_files(): st.session_state.display_page = 'share_data_files'
def page_volume_page(): st.session_state.display_page = 'volume'
def page_analysis(): st.session_state.display_page = 'analysis'
def page_scope(): st.session_state.display_page = 'scope'

# Sidebar Action Buttons ======================================================================================= 
st.sidebar.title(project_description)
st.sidebar.button(('Share Index ( ' + str((len(st.session_state.share_index_file))) + ' )'), on_click=page_share_index)

# Select Tickers -----------------------------------------------------------------------------------------------
st.sidebar.subheader('Ticker List Selectors - choose tickers')
market   = st.sidebar.selectbox  ('Add Entire Market to ticker list'  , st.session_state.available_markets   , on_change=update_ticker_list_required, help='Select an Entire Share Market for Analysis')
industry = st.sidebar.multiselect('Add Industry(s) to the ticker list', st.session_state.available_industries, on_change=update_ticker_list_required, help='Quickly Select all tickers in a particular industry')
tickers  = st.sidebar.multiselect('Add Ticker(s) to the ticker list'  , st.session_state.available_tickers   , on_change=update_ticker_list_required, help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list') 

# Update the ticker list if required (selector box has changed)
if st.session_state.update_ticker_list_required:
	st.session_state.selected_market = market
	st.session_state.selected_industry = industry
	st.session_state.selected_tickers = tickers
	construct_list_of_share_codes(st.session_state)

# ticker list and ticker data buttons
st.sidebar.button( ('Show Ticker List ( ' + str((len(st.session_state.ticker_list))) + ' )'), on_click=page_show_ticker_list )
st.sidebar.button( ('Load and Import Share Data'), on_click=page_manage_share_data)
st.sidebar.button( ('Show Share Data Files ( ' + str(len(st.session_state.share_data_files.keys())) + ' )'), on_click=page_share_data_files)

# Analysis Pages -----------------------------------------------------------------------------------------------
st.sidebar.subheader('Analysis')
# st.sidebar.info('Ticker List ( ' + str((len(st.session_state.ticker_list))) + ' )')
st.sidebar.button('Volume Analysis', on_click=page_volume_page)
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