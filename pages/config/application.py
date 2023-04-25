
import streamlit as st
from datetime import datetime 

from pages.config.three_cols import three_cols


def render_scope_config(scope):

	st.subheader('Application Configuration')
	three_cols( 'Application Configuration stored in', {}, "scope.config", widget_type='string' )

	st.write('---')	
	st.caption('Application')
	three_cols( 'Project Description', 
	    		scope.config['project_description'], 
				"scope.config['project_description']" )
	start_time =  datetime.fromtimestamp(scope.config['project_start_time']).strftime('%Y-%m-%d %H:%M:%S %p')
	three_cols( 'Project Start Time', 
	    		start_time, 
				"scope.config['project_start_time']" )



