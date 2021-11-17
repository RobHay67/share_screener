
import streamlit as st


from system.view import view_3_columns


def scope_user(scope):
	scope.download_days 		= 5
	scope.analysis_row_limit 	= 100
	scope.chart_height			= 2000


def view_user(scope):
	
	st.header('User Setting')
	
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns([2.0,2.0,2.0,1.1,1.2,1.2,1.0,1.5,1.0])
	
	with col1: st.subheader('Download Days')
	with col1: view_download_days(scope)

	with col2: st.subheader('Analysis Row Limit')
	with col2: view_analysis_row_limit(scope)

	with col3: st.subheader('Chart Height (pixels)')
	with col3: view_chart_height(scope)



	st.markdown("""---""")


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render User Settings and Variables
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_download_days(scope):

	previous_selection = int(scope.download_days)

	input_download_days = st.number_input( 
											'Number of most recent business days to download from Y_Finance', 
											min_value=1, 
											value=previous_selection, 						# Default Value to display (would revert on every second try)
											key='97'
											)   
	scope.download_days = input_download_days


def view_analysis_row_limit(scope): # limit_analysis

	previous_selection = int(scope.analysis_row_limit)

	input_analysis_days = st.number_input( 	
										'limit analysis dataframes to this many rows (by date - most recent)', 
										min_value=0, 
										value=previous_selection,
										key='95'
										)  
	scope.analysis_row_limit = input_analysis_days

def view_chart_height(scope): # limit_analysis

	previous_selection = int(scope.chart_height)

	input_chart_height = st.number_input( 	
										'Adjust height of chart section (depends on your resolution)', 
										min_value=0, 
										value=previous_selection,
										key='95'
										)  
	scope.chart_height = input_chart_height