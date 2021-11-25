import streamlit as st

from views.scope_var import three_cols


def view_app(scope):

	st.subheader('Share Market')
	three_cols( 'Current Share Market <hard coded>', scope.share_market, 'share_market' )

	st.subheader('Behavioural')
	three_cols( 'Initial Load ?', scope.initial_load, 'initial_load' )
	three_cols( 'Current Page to Display', scope.page_to_display, 'display_page' )
	three_cols( 'Do the Dropdown Lists Need Refreshing ?', scope.dropdown_lists_need_updating, 'dropdown_lists_need_updating' )
	
	st.subheader('Streamlit Reusable Variables')
	three_cols( 'Streamlit Latest Button Pressed', scope.st_button, 'st_button' )

