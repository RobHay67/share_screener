
import streamlit as st
from datetime import datetime 

from pages.config.three_cols import three_cols
from pages.header.page_config import view_page_config


def render_scope_config(scope):

	st.subheader('Application Configuration')
	three_cols( 'Application Configuration stored in', 
	    		{}, 
				'scope.config', widget_type='string' )

	st.subheader('Application')
	three_cols( 'Project Description', 
	    		scope.config['project_description'], 
				'scope.config.project_description' )
	start_time =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	three_cols( 'Project Start Time', 
	    		start_time, 
				'scope.config.project_start_time' )

	st.subheader('Share Market')
	three_cols( 'Current Share Market', 
	    		scope.config['share_market'], 
				'scope.config.share_market' )

	st.subheader('Days to Download')
	three_cols( 'Days to Download (recent)',
	    		 scope.config['download_days'], 
				 "scope.config['download_days']" )

	st.subheader('System')
	three_cols( 'Current Page to Display', 
	    		scope.pages['display'], 
				"scope.pages['display']" )

	st.write('---')
	view_page_config(scope)

