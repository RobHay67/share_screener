import streamlit as st


# -----------------------------------------------------------------------------------------------------------------------------------
# Output Ticker Iteration to Browser
# -----------------------------------------------------------------------------------------------------------------------------------




def view_results(scope):
	with scope.col6:
		if scope.results['passed_count'] > 0: st.info(scope.results['passed'])
		if scope.results['passed_2_count'] > 0: st.warning(scope.results['passed_2'])
		if scope.results['failed_count'] > 0: st.error(scope.results['failed'])


def download_industry_message(scope, message):
	with scope.col6:
		st.write(  message )



