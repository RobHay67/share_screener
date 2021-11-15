import streamlit as st

from system.view import view_3_columns

def scope_app(scope):
	# System Wide Variables
	scope.share_market = 'ASX'					# Set Initial Default Share Market - we gotta start somewhere
	scope.display_page = 'initial_load'			# The homepage to display on first load
	scope.dropdown_lists_need_updating = False	# Intially set to false, the loading or refreshing of the 
													# share index file has resposibility to set this, but can
													# only do this after loading the share index file
	scope.st_button = None

def view_app(scope):
	st.subheader('Share Market')
	view_3_columns( 'Current Share Market <hard coded>', scope.share_market, 'share_market' )

	st.subheader('Behavioural')
	view_3_columns( 'Initial Load ?', scope.initial_load, 'initial_load' )
	view_3_columns( 'Current Page to Display', scope.display_page, 'display_page' )
	view_3_columns( 'Do the Dropdown Lists Need Refreshing ?', scope.dropdown_lists_need_updating, 'dropdown_lists_need_updating' )
	
	st.subheader('Streamlit Reusable Variables')
	view_3_columns( 'Streamlit Latest Button Pressed', scope.st_button, 'st_button' )

