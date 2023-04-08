
import streamlit as st
from datetime import datetime 

from pages.config.three_cols import three_cols
from pages.header.page_config import view_app_page_config


def view_app(scope):

	st.subheader('Application Configuration')
	three_cols( 'Application Configuration stored in', {}, 'scope.config', widget_type='string' )

	st.subheader('Application')
	three_cols( 'Project Description', scope.config['project_description'], 'scope.config.project_description' )
	start_time =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	three_cols( 'Project Start Time', start_time, 'scope.config.project_start_time' )

	st.subheader('Share Market')
	three_cols( 'Current Share Market', scope.config['share_market'], 'scope.config.share_market' )

	st.subheader('System')
	three_cols( 'Initial Load ?', scope.initial_load, 'initial_load' )
	
	st.write('---')
	view_app_page_config(scope)

