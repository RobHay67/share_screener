import streamlit as st


# -----------------------------------------------------------------------------------------------------------------------------------
# Output Results
# -----------------------------------------------------------------------------------------------------------------------------------

def view_result(scope):
	with scope.col6:
		if scope.progress['passed_count'] > 0: st.info(scope.progress['passed'])
		if scope.progress['passed_2_count'] > 0: st.warning(scope.progress['passed_2'])
		if scope.progress['failed_count'] > 0: st.error(scope.progress['failed'])


def download_industry_message(scope, message):
	with scope.col6:
		st.write(  message )




