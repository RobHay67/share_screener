import streamlit as st

from views.scope_var import three_cols



def view_results(scope):
	st.subheader('Results from Most Recent Batch Process')
	st.markdown("""---""")
	st.subheader('Result Parameters')
	three_cols( 'Result Passed', scope.results['passed'], "result['passed']" )
	three_cols( 'Result Passed_2', scope.results['passed_2'], "result['passed_2']" )
	three_cols( 'Result Failed', scope.results['failed'], "result['failed']" )
	three_cols( 'Count Passed', scope.results['passed_count'], "result['passed_count']" )
	three_cols( 'Count Passed_2', scope.results['passed_2_count'], "result['passed_2_count']" )
	three_cols( 'Count Failed', scope.results['failed_count'], "result['failed_count']" )


