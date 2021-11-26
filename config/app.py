import time  



def scope_app(scope):
	# Application Fixex Variables
	scope.project_description = 'DDT - Data Driven Trading'
	scope.project_start_time = time.time()


	# System Wide Variables
	scope.share_market = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere
	scope.dropdown_lists_need_updating = False		# Intially set to false, the loading or refreshing of the 
													# share index file has resposibility to modify this, but can
													# only do this after loading the share index file
	
	scope.st_button = None







import streamlit as st
from datetime import datetime 

from pages.view.three_cols import three_cols


def view_app(scope):
	st.subheader('Application')
	three_cols( 'Project Description', scope.project_description, 'project_description' )
	three_cols( 'Project Start Time', datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )


	st.subheader('Share Market')
	three_cols( 'Current Share Market <hard coded>', scope.share_market, 'share_market' )

	st.subheader('Behavioural')
	three_cols( 'Initial Load ?', scope.initial_load, 'initial_load' )
	three_cols( 'Current Page to Display', scope.page_to_display, 'display_page' )
	three_cols( 'Do the Dropdown Lists Need Refreshing ?', scope.dropdown_lists_need_updating, 'dropdown_lists_need_updating' )
	
	st.subheader('Streamlit Reusable Variables')
	three_cols( 'Streamlit Latest Button Pressed', scope.st_button, 'st_button' )




