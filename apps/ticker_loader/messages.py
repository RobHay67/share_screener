import streamlit as st


# -----------------------------------------------------------------------------------------------------------------------------------
# Output Results
# -----------------------------------------------------------------------------------------------------------------------------------

def view_result(scope):
	with scope.col6:
		if scope.config['results']['passed_count'] > 0: st.info(scope.config['results']['passed'])
		if scope.config['results']['passed_2_count'] > 0: st.warning(scope.config['results']['passed_2'])
		if scope.config['results']['failed_count'] > 0: st.error(scope.config['results']['failed'])


def download_industry_message(scope, message):
	with scope.col6:
		st.write(  message )




