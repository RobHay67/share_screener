# streamlit run app.py

project_description = 'Share Trader - DDT'


# from scope import set_initial_scope, build_ticker_dropdowns, render_scope_page

from scope import set_initial_scope
from scope import build_ticker_dropdowns
from scope import render_scope_page
from share_index import load_share_index_file, render_share_index_page
from share_data import render_share_data_page
from ticker_list import render_home_page, construct_list_of_share_codes
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

if   st.session_state.display_page == 'home': render_home_page(st.session_state)
elif st.session_state.display_page == 'volume':	render_volume_page(st.session_state)    
elif st.session_state.display_page == 'share_index': render_share_index_page(st.session_state)
elif st.session_state.display_page == 'share_data_files': render_share_data_page(st.session_state)
elif st.session_state.display_page == 'analysis': st.title('Analysis')
elif st.session_state.display_page == 'scope': render_scope_page(st.session_state)

# Call Backs for Sidebar Action Buttons ========================================================================= 
def show_home_page(): st.session_state.display_page = 'home'
def show_share_index_page(): st.session_state.display_page = 'share_index'
def update_ticker_list_required(): st.session_state.update_ticker_list_required = True
def show_share_data_files_page(): st.session_state.display_page = 'share_data_files'
def show_volume_page(): st.session_state.display_page = 'volume'
def show_analysis_page(): st.session_state.display_page = 'analysis'
def show_scope_page(): st.session_state.display_page = 'scope'
# Sidebar Action Buttons ======================================================================================= 
st.sidebar.title(project_description)
st.sidebar.button('Home Page......', on_click=show_home_page)
st.sidebar.subheader('Loaded Data')
st.sidebar.button(('Share Index ( ' + str((len(st.session_state.share_index_file))) + ' )'), on_click=show_share_index_page)

# Select Tickers -----------------------------------------------------------------------------------------------
st.sidebar.subheader('Ticker List - add tickers')
market   = st.sidebar.selectbox  ('Add Entire Market to ticker list'  , st.session_state.available_markets   , on_change=update_ticker_list_required, help='Select an Entire Share Market for Analysis')
industry = st.sidebar.multiselect('Add Industry(s) to the ticker list', st.session_state.available_industries, on_change=update_ticker_list_required, help='Quickly Select all tickers in a particular industry')
tickers  = st.sidebar.multiselect('Add Ticker(s) to the ticker list'  , st.session_state.available_tickers   , on_change=update_ticker_list_required, help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list') 
# Update the ticker list if required (selector box has changed)
if st.session_state.update_ticker_list_required:
	st.session_state.selected_market = market
	st.session_state.selected_industry = industry
	st.session_state.selected_tickers = tickers
	construct_list_of_share_codes(st.session_state)
	# print(tickers)
	# print ( 'selected_tickers = ', st.session_state.selected_tickers ) 
st.sidebar.button(('Share Data Files ( ' + str((len(st.session_state.ticker_list))) + ' )'), on_click=show_share_data_files_page)




# Analysis Pages -----------------------------------------------------------------------------------------------
st.sidebar.subheader('Analysis')
# st.sidebar.info('Ticker List ( ' + str((len(st.session_state.ticker_list))) + ' )')
st.sidebar.button('Volume Analysis', on_click=show_volume_page)
st.sidebar.button('Perform Analysis', on_click=show_analysis_page)


# System Variables ---------------------------------------------------------------------------------------------
st.sidebar.subheader('System Variables')
st.sidebar.button('Scope Variables', on_click=show_scope_page)











# print( 'List of all keys in the st.session_state')
# if 'initial_load' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)