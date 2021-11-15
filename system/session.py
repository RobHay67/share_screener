import streamlit as st

from system.reports import render_3_columns
from ticker.files import selected_tickers_for_each_page



def scope_session(scope):
	# System Wide Variables
	scope.share_market = 'ASX'					# Set Initial Default Share Market - we gotta start somewhere
	scope.display_page = 'initial_load'			# The homepage to display on first load
	scope.dropdown_lists_need_updating = False	# Intially set to false, the loading or refreshing of the 
													# share index file has resposibility to set this, but can
													# only do this after loading the share index file
	scope.st_button = None

	# Download Ticker Variables # TODO - Move this to a module when finished
	scope.download_days 			= 5
	scope.download_industries 		= []
	scope.download_yf_files			= {}
	scope.downloaded_loaded_list 	= []
	scope.downloaded_missing_list 	= []
	scope.downloaded_yf_anomolies 	= {}

	# Analysis Variables
	scope.analysis_limit_share_data = 300
	# scope.analysis_apply_limit = False

def render_session(scope):
	st.subheader('Share Market')
	render_3_columns( 'Current Share Market <hard coded>', scope.share_market, 'share_market' )

	st.subheader('Behavioural')
	render_3_columns( 'Initial Load ?', scope.initial_load, 'initial_load' )
	render_3_columns( 'Current Page to Display', scope.display_page, 'display_page' )
	render_3_columns( 'Do the Dropdown Lists Need Refreshing ?', scope.dropdown_lists_need_updating, 'dropdown_lists_need_updating' )
	
	st.subheader('Streamlit Reusable Variables')
	render_3_columns( 'Streamlit Latest Button Pressed', scope.st_button, 'st_button' )

def render_download(scope):

	st.markdown('##### Download Variables')
	render_3_columns( 'Number of Days to Download', scope.download_days, 'download_days' )

	st.markdown('##### Most Recent Download Variables and Data')
	render_3_columns( 'Industry Groups for y_finance to iterate over', scope.download_industries, 'download_industries' )
	render_3_columns( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )
	render_3_columns( 'Missing Ticker List', scope.downloaded_missing_list, 'downloaded_missing_list' )
	render_3_columns( 'Latest Download Batch from y_finance', scope.download_yf_files, 'download_yf_files' )
	render_3_columns( 'Latest Error Messages from y_finance', scope.downloaded_yf_anomolies  , 'downloaded_yf_anomolies' )

	selected_tickers_for_each_page(scope)
	render_3_columns( 'Current Ticker List', '', "ticker_list['page']" )
	st.write('Most Recent Download came from the above tickers depending on the originating page')


