import streamlit as st

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Welcome Page # TODO - this should be a page or the system variables page - nice i like this idea
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_project_welcome(scope):
	st.title(scope.project_description)
	st.success('Loaded and Ready for Analysis')



