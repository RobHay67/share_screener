# streamlit run app.py

project_description = 'Share Trader - DDT'



from session_vars import set_initial_session_state, render_sidebar_drop_down_lists, render_app_params_selector
from share_index import load_share_index_file

from page_home import render_home_page, construct_list_of_share_codes
from page_share_data import render_share_data_page
# from share_data import render_share_data_page


# Set Up Streamlit Environment ==================================================================================
import streamlit as st
st.set_page_config(layout="wide")
set_initial_session_state(st.session_state, project_description)
if st.session_state.first_render_of_streamlit == True:
	load_share_index_file(st.session_state)
render_sidebar_drop_down_lists(st.session_state)
st.session_state.first_render_of_streamlit = False
# ===============================================================================================================
print ( '='*100)
print ( 'A Refresh of the application has occured')
print ( '-'*100)
# print( 'List of all keys in the st.session_state')
# if 'first_render_of_streamlit' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)


# Display Appropriate Page ====================================================================================== 
# print ( 'Current Page = ', st.session_state.display_page)

if st.session_state.display_page == 'home': render_home_page(st.session_state)
elif st.session_state.display_page == 'volume':
	st.title('Volume Analysis')
elif st.session_state.display_page == 'download': render_share_data_page(st.session_state)
elif st.session_state.display_page == 'app_params':
	render_app_params_selector(st.session_state)

# Call Backs for Sidebar Action Buttons ========================================================================= 
def update_ticker_list(): st.session_state.ticker_list_needs_updating = True
def show_home_page(): st.session_state.display_page = 'home'
def show_volume_page(): st.session_state.display_page = 'volume'
def show_download_page(): st.session_state.display_page = 'download'
def show_params_page(): st.session_state.display_page = 'app_params'


# Sidebar Action Buttons ======================================================================================= 
st.sidebar.title(project_description)
st.sidebar.button('Home Page......', on_click=show_home_page)
st.sidebar.button('Volume Analysis', on_click=show_volume_page)
# Select Tickers -----------------------------------------------------------------------------------------------
market   = st.sidebar.selectbox  ('Add Entire Market to ticker list'  , st.session_state.available_markets   , on_change=update_ticker_list, help='Select an Entire Share Market for Analysis')
industry = st.sidebar.multiselect('Add Industry(s) to the ticker list', st.session_state.available_industries, on_change=update_ticker_list, help='Quickly Select all tickers in a particular industry')
tickers  = st.sidebar.multiselect('Add Ticker(s) to the ticker list'  , st.session_state.available_tickers   , on_change=update_ticker_list, help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list') 

# Update the ticker list if required (selector box has changed)
if st.session_state.ticker_list_needs_updating:
	st.session_state.selected_market = market
	st.session_state.selected_industry = industry
	st.session_state.selected_tickers = tickers
	construct_list_of_share_codes(st.session_state)

# Pages ------------------------------------------------------------------------------------------------------- 
st.sidebar.button('Load Share Data', on_click=show_download_page)
st.sidebar.button('Analysis', on_click=show_volume_page)
st.sidebar.button('Application Parameters', on_click=show_params_page)

