
import streamlit as st
from datetime import datetime 

from apps.config_app.three_cols import three_cols


def view_app(scope):
	st.subheader('Application')
	three_cols( 'Project Description', scope.config['project_description'], 'scope.config.project_description' )

	start_time =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	three_cols( 'Project Start Time', start_time, 'scope.config.project_start_time' )

	st.subheader('Share Market')
	three_cols( 'Current Share Market', scope.config['share_market'], 'scope.config.share_market' )

	st.subheader('System')
	three_cols( 'Initial Load ?', scope.initial_load, 'initial_load' )
	

