import streamlit as st


from page.config.application import scope_application_variables
from page.config.dropdowns import scope_dropdown_menus
from files.config import scope_folders_and_paths
from users.config import scope_users
from page.config.pages import scope_pages
from trials.config import scope_trials
from charts.config import scope_charts
from ticker_index.config import scope_index_file
from page.config.ticker_search import scope_ticker_search
from tickers.config import scope_tickers
from tickers.config import scope_tickers_missing
from y_finance.config import scope_download_variables
from strategies.config import scope_strategy


def set_scope(scope):

	set_streamlit_page_config()								# should only run onetime
	
	if 'display_page' not in scope:	
		scope.user_autologin = True				# TODO for releases purposes only - delete later
		scope.display_page = 'home'			# Prevent session_state/scope from reloading with the default values
		scope_application_variables(scope)	# This contains all the application settings (see below)	
		scope_dropdown_menus(scope)			# The data for the various selectors
		scope_folders_and_paths(scope)		# Required before we can attempt to load the data
		scope_users(scope)					# Set Default Values ready for a user to login
		scope_pages(scope)					# This contains all the page Specific settings
		scope_trials(scope)					# add the trials configuration
		scope_charts(scope)					# add the chart configuration
		scope_index_file(scope)				# load the share index
		scope_ticker_search(scope)			# variable to facilite searching for ticker by name
		scope_tickers(scope)				# variables for storing the ticker files
		scope_tickers_missing(scope)		# track missing tickers and associated errors
		scope_download_variables(scope)		# variable used during download of ticker data
		scope_strategy(scope)				# TODO - this may not even be required - keeping just in case

	return scope

	

def set_streamlit_page_config():
	
	# Set the Browser Tab Name for the Page
	st.set_page_config( 
			page_title='Share Picker', 
			page_icon='📊',
			layout="wide",								# Allow wide Screen to be taken advantage of
			)
	
	# Padding Between Controls
	padding = 1.0
	st.markdown(f""" <style>
		.reportview-container .main .block-container{{
			padding-top: {padding}rem;
			padding-right: {padding}rem;
			padding-left: {padding}rem;
			padding-bottom: {padding}rem;
		}} </style> """, unsafe_allow_html=True)

	# Remove whitespace from the top of the page and sidebar
	st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True) # this is heaps better
	# st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
	# st.markdown("""
	# 				<style>
	# 					.css-o18uir.e16nr0p33 {
	# 					margin-top: -75px;
	# 					}
	# 				</style>
	# 				""", unsafe_allow_html=True)

	# st.markdown(
    #         f'''
    #         <style>
    #             .reportview-container .sidebar-content {{
    #                 padding-top: {1}rem;
    #             }}
    #             .reportview-container .main .block-container {{
    #                 padding-top: {1}rem;
    #             }}
    #         </style>
    #         ''',unsafe_allow_html=True)


	# st.markdown("""
    #     <style>
    #         #    .css-18e3th9 {
    #         #         padding-top: 0rem;
    #         #         padding-bottom: 10rem;
    #         #         padding-left: 5rem;
    #         #         padding-right: 5rem;
    #         #     }
    #         #    .css-1d391kg {
    #         #         padding-top: 1rem;
    #         #         padding-right: 1rem;
    #         #         padding-bottom: 3.5rem;
    #         #         padding-left: 1rem;
    #         #     }
    #     </style>
    #     """, unsafe_allow_html=True)

