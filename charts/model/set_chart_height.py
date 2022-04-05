import streamlit as st





def set_chart_height_primary(scope):

	# st.subheader('Chart Height (pixels)')

	previous_selection = int(scope.config['charts']['primary_height'])

	input_chart_height = st.number_input( 	
										'Primary Chart Height', 
										min_value=0, 
										value=previous_selection,
										key='95'
										)  
	scope.config['charts']['primary_height'] = input_chart_height



