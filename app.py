# streamlit run app.py

project_description = 'Share Trader - DDT'



from params import set_initial_session_state, render_sidebar_drop_down_lists, render_app_params_selector
from share_index import load_share_index_file

from home_page import render_home_page, construct_list_of_share_codes


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
# print ( 'session_state.first_render_of_streamlit = ', st.session_state.first_render_of_streamlit )
# print ( 'session_state.display_page = ', st.session_state.display_page )
# if 'ticker_list' in st.session_state:
# 	print ('ticker list in session is this long ', len(st.session_state.ticker_list))
# print ( '*'*100)
# print( 'List of all keys in the st.session_state')
# if 'first_render_of_streamlit' in st.session_state:
# 	print(st.session_state)
# 	for key in sorted(st.session_state):
# 		print ( key)
# print ( '-'*100)


# Display Appropriate Page ====================================================================================== 
# print ( 'Current Page = ', st.session_state.display_page)

if st.session_state.display_page == 'home':
	render_home_page(st.session_state)
elif st.session_state.display_page == 'volume':
	st.title('Volume Analysis')
elif st.session_state.display_page == 'download':
	st.title('Download Share Data')
elif st.session_state.display_page == 'app_params':
	render_app_params_selector(st.session_state)
	


# Call Backs for Sidebar Action Buttons ========================================================================= 
def update_ticker_list():
	st.session_state.ticker_list_needs_updating = True
	
def show_home_page():
	st.session_state.display_page = 'home'

def show_volume_page():
	st.session_state.display_page = 'volume'

def show_download_page():
	st.session_state.display_page = 'download'

def show_params_page():
	st.session_state.display_page = 'app_params'


# Sidebar Action Buttons ======================================================================================= 
st.sidebar.button('Home Page', on_click=show_home_page)
# Select Tickers -----------------------------------------------------------------------------------------------
st.sidebar.title(project_description)
# st.sidebar.subheader('Select Tickers')
market = st.sidebar.selectbox  ('Select Entire Market', st.session_state.available_markets, on_change=update_ticker_list, help='Select an Entire Share Market for Analysis')
industry = st.sidebar.multiselect('Select An Industry', st.session_state.available_industries, on_change=update_ticker_list, help='Quickly Select all tickers in a particular industry')
tickers = st.sidebar.multiselect('Select Ticker(s)', st.session_state.available_tickers, on_change=update_ticker_list, help='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list') 


if st.session_state.ticker_list_needs_updating:
	st.session_state.selected_market = market
	st.session_state.selected_industry = industry
	st.session_state.selected_tickers = tickers
	construct_list_of_share_codes(st.session_state)

st.sidebar.button('Analysis', on_click=show_volume_page)
# Pages ------------------------------------------------------------------------------------------------------- 

st.sidebar.button('Volume Analysis', on_click=show_volume_page)
st.sidebar.button('Download Fresh Share Data', on_click=show_download_page)
st.sidebar.button('Application Parameters', on_click=show_params_page)

