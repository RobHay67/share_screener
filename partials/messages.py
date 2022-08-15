import streamlit as st


# -----------------------------------------------------------------------------------------------------------------------------------
# Output Results
# -----------------------------------------------------------------------------------------------------------------------------------

def render_messages(scope):
	with scope.col5:
		if scope.progress['passed_count'] > 0: 
			st.info(scope.progress['passed'])
		if scope.progress['passed_2_count'] > 0: 
			st.warning(scope.progress['passed_2'])
		if scope.progress['failed_count'] > 0: 
			st.error(scope.progress['failed'])


def download_industry_message(scope, message):
	with scope.col5:
		st.write(  message )


def clear_messages_button(scope):

	with scope.col5: 
		st.button('Clear Messages')


