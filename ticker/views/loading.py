


import streamlit as st



def load_columns(scope, page):
	if page == 'multi':
		col1,col2,col3,col4,col5,col6 = st.columns([2.0, 3.4, 0.1, 1.5, 2.0, 3.0])
	else:
		col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 1.5, 1.5, 2.0, 3.0])
	
	scope.col1 = col1
	scope.col2 = col2
	scope.col3 = col3
	scope.col4 = col4
	scope.col5 = col5
	scope.col6 = col6


def view_results(scope):
	
	with scope.col6:
		if scope.results['passed_count'] > 0: st.info(scope.results['passed'])
		if scope.results['passed_2_count'] > 0: st.warning(scope.results['passed_2'])
		if scope.results['failed_count'] > 0: st.error(scope.results['failed'])


def download_industry_message(scope, message):
	with scope.col6:
		st.write(  message )