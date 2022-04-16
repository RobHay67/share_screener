import streamlit as st

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Welcome Page # TODO - this should be a page or the system variables page - nice i like this idea
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_project_welcome(scope):

	if scope.initial_load == True:
		st.title(scope.config['project_description'])
	else:
		st.success('Configured and Ready for Analysis')




