import streamlit as st

from apps.config_app.three_cols import three_cols


def view_all_results(scope):
	st.subheader('Results from Most Recent Batch Process')
	st.markdown("""---""")
	st.subheader('Result Parameters')
	three_cols( 'Result Passed', scope.progress['passed'], "result['passed']" )
	three_cols( 'Result Passed_2', scope.progress['passed_2'], "result['passed_2']" )
	three_cols( 'Result Failed', scope.progress['failed'], "result['failed']" )
	three_cols( 'Count Passed', scope.progress['passed_count'], "result['passed_count']" )
	three_cols( 'Count Passed_2', scope.progress['passed_2_count'], "result['passed_2_count']" )
	three_cols( 'Count Failed', scope.progress['failed_count'], "result['failed_count']" )

