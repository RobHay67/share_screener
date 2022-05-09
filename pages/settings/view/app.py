
import streamlit as st
from datetime import datetime 

from config.results.three_cols import three_cols


def view_app(scope):
	st.subheader('Application')
	three_cols( 'Project Description', scope.config['project_description'], 'project_description' )
	three_cols( 'Project Start Time', datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )


	st.subheader('Share Market')
	three_cols( 'Current Share Market <hard coded>', scope.config['share_market'], 'share_market' )

	st.subheader('Behavioural')
	three_cols( 'Initial Load ?', scope.initial_load, 'initial_load' )
	three_cols( 'Current Page to Display', scope.pages['display_page'], 'display_page' )
	three_cols( 'Do the Dropdown Lists Need Refreshing ?', scope.config['dropdowns']['update_dropdowns'], 'dropdown_lists_need_updating' )
	
	st.subheader('Streamlit Reusable Variables')
	three_cols( 'Streamlit Latest Button Pressed', scope.pages['button_for_scope'], 'button_for_scope' )




