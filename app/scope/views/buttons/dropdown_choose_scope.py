
import streamlit as st

# list(scope.charts['schema'].keys())
# chart = next(iter(scope.charts['user_config'].keys()))


def scope_dropdown(scope, list_options):

	scope_dropdown = st.selectbox(
		label='Select from the Dropdown Menu',
		options=list_options,
		index=0,
		)
	
	return scope_dropdown

