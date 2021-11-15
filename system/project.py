import streamlit as st
import time  
from datetime import datetime 

from system.view import view_3_columns

def scope_project(scope, project_description):
	scope.project_description = project_description
	scope.project_start_time = time.time()


def view_project(scope):
	st.subheader('General Application Parameters')
	view_3_columns( 'Project Description', scope.project_description, 'project_description' )
	view_3_columns( 'Project Start Time', datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Welcome Page # TODO - this should be a page or the system variables page - nice i like this idea
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_project_welcome(scope):
	st.title(scope.project_description)
	st.success('Loaded and Ready for Analysis')







