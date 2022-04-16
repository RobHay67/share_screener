
import streamlit as st




def view_test_results(scope):

	st.write('**Test Results**')

	# page = scope.pages['display_page']

	all_test_results_df = scope.pages['tests']['df']

	print(all_test_results_df)

	if len(all_test_results_df) > 0:
		passed_test_results_df = all_test_results_df[all_test_results_df['all_test_results'] == 'passed']
		failed_test_results_df = all_test_results_df[all_test_results_df['all_test_results'] == 'failed']
		
	else:
		passed_test_results_df = {}
		failed_test_results_df = {}

	my_expander = st.expander(label='Passed All Tests', expanded=True )
	my_expander.dataframe(passed_test_results_df, 2000, 2000)	

	my_expander = st.expander(label='Failed All Tests', expanded=False )
	my_expander.dataframe(failed_test_results_df, 2000, 2000)	

	my_expander = st.expander(label='All Test Results', expanded=False )
	my_expander.dataframe(all_test_results_df, 2000, 2000)	


	# my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded )
	# my_expander.dataframe(ticker_data_file, 2000, 2000)	