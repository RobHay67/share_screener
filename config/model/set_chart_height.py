import streamlit as st





def set_primary_chart_height(scope):

	# st.subheader('Chart Height (pixels)')

	previous_selection = int(scope.primary_chart_height)

	input_chart_height = st.number_input( 	
										'Primary Chart Height', 
										min_value=0, 
										value=previous_selection,
										key='95'
										)  
	scope.primary_chart_height = input_chart_height



