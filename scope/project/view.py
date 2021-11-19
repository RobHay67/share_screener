import streamlit as st
from datetime import datetime 


from views.scope_var import three_cols

def view_project(scope):
	st.subheader('General Application Parameters')
	three_cols( 'Project Description', scope.project_description, 'project_description' )
	three_cols( 'Project Start Time', datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )









