import streamlit as st


def view_analysis(scope):
	
	st.header('Analysis Setting')
	
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns([2.0,2.0,2.0,1.1,1.2,1.2,1.0,1.5,1.0])

	with col2: st.subheader('Analysis Row Limit')
	with col2: set_analysis_row_limit(scope)

	st.markdown("""---""")




def set_analysis_row_limit(scope):

	page = scope.page_to_display

	previous_selection = int(scope.analysis_row_limit)

	input_analysis_days = st.number_input( 	
										'No of Rows for Analysis', 
										min_value=0, 
										value=previous_selection,
										key='95'
										)  
	

	if input_analysis_days != previous_selection:
		# Store the Result
		scope.analysis_row_limit = input_analysis_days

		# reset STATUS to prevent unnecesary updates 
		# (as this applies to all pages - they all need a refresh)
		for page in scope.pages:
			scope.pages[page]['refresh_analysis_df'] = True


