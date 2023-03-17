import streamlit as st



def add_columns_button(scope):
		
		app = scope.apps['display_app']

		# Prevent col calculation until the appropriate time/event
		replace_columns = False

		if app == 'screener': 
			replace_columns = st.button(
									label='Run Tests', 
									use_container_width=True, 
									type='primary'
									)
		else:
			# Manually trigger replace_columns
			# TODO - this may not need to run on some screens
			replace_columns = True
			st.button(
									label='Rates & Ratios', 
									use_container_width=True, 
									disabled=True,
									)
						
		return replace_columns
			