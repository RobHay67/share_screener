import streamlit as st

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Welcome Page # TODO - this should be a page or the system variables page - nice i like this idea
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_project_welcome(scope):

	if scope.initial_load == True:
		st.title(scope.project_description)
	else:
		st.success('Configured, loaded share index file and Ready for Analysis')



