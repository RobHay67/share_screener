import streamlit as st

from pages.view.three_cols import three_cols




def scope_results(scope):
	# Results - for batch processing of multiple tickers
	scope.config['results'] = {}

	scope.config['results'] = { 
								'passed':'', 
								'passed_2':'', 
								'failed':'', 
								'passed_count':0, 
								'passed_2_count':0, 
								'failed_count':0 
							}


def view_results(scope):
	st.subheader('Results from Most Recent Batch Process')
	st.markdown("""---""")
	st.subheader('Result Parameters')
	three_cols( 'Result Passed', scope.config['results']['passed'], "result['passed']" )
	three_cols( 'Result Passed_2', scope.config['results']['passed_2'], "result['passed_2']" )
	three_cols( 'Result Failed', scope.config['results']['failed'], "result['failed']" )
	three_cols( 'Count Passed', scope.config['results']['passed_count'], "result['passed_count']" )
	three_cols( 'Count Passed_2', scope.config['results']['passed_2_count'], "result['passed_2_count']" )
	three_cols( 'Count Failed', scope.config['results']['failed_count'], "result['failed_count']" )


