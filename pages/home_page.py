import streamlit as st


def render_project_welcome(scope):

	if scope.initial_load == True:
		st.title(scope.config['project_description'])
	else:
		st.success('Configured and Ready for Analysis')




