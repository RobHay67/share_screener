import streamlit as st
import time  
from datetime import datetime 

from system.reports import render_3_columns

def scope_project(scope, project_description):
	scope.project_description = project_description
	scope.project_start_time = time.time()


def render_project(scope):
	st.subheader('General Application Parameters')
	render_3_columns( 'Project Description', scope.project_description, 'project_description' )
	render_3_columns( 'Project Start Time', datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )



