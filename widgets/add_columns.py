import streamlit as st



def add_columns_button(scope):
		
		app = scope.apps['display_app']
		button_label='Add Columns'
		button_disabled = True

		if app == 'screener': 
			button_label='Run Tests'
			button_disabled=False
		if app=='chart':
			button_label='Add Metrics'

		button = st.button(
								label=button_label, 
								use_container_width=True, 
								type='primary',
								disabled=button_disabled,
								)

		return button
			