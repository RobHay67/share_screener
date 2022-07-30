
import streamlit as st

from config.tests.results import create_summary_of_test_results



def render_test_results(scope):

	st.write('**Test Results**')

	test_results_df = create_summary_of_test_results(scope)	

	if len(test_results_df) > 0:
		passed_test_results_df = test_results_df[test_results_df['summary_result'] == 'pass']
		failed_test_results_df = test_results_df[test_results_df['summary_result'] == 'fail']
		
	else:
		passed_test_results_df = {}
		failed_test_results_df = {}

	col1,col2,col3 = st.columns([4,4,4])


	no_columns = len(test_results_df.columns)

	pixel_width = 70 * no_columns
	pixel_row_height = 40

	with col1:
		no_passed = str(len(passed_test_results_df))
		my_expander = st.expander(label='Passed Every Test (' + no_passed + ' )', expanded=False )
		my_expander.dataframe(passed_test_results_df, pixel_width, len(passed_test_results_df)*pixel_row_height)	
	with col2:
		no_failed = str(len(failed_test_results_df))
		my_expander = st.expander(label='Failed Every Test (' + no_failed + ' )', expanded=False )
		my_expander.dataframe(failed_test_results_df, pixel_width, len(failed_test_results_df)*pixel_row_height)	
	with col3:
		no_tested = str(len(test_results_df))
		my_expander = st.expander(label='Every Test Result (' + no_tested + ' )', expanded=False )
		my_expander.dataframe(test_results_df, pixel_width, len(test_results_df)*pixel_row_height)	
















	# The original render test results
	# TODO - delete after getting the tests working


	# def render_test_results(scope):

	# 	st.write('**Test Results**')

	# 	print('X'*66)

	# 	# App = scope.apps['display_app']

	# 	test_results_df = scope.apps['tests']['df']
	# 					#   scope.apps['tests']['df'] = test_results_df

	# 	# print('.'*77)
	# 	print('test_results_df')
	# 	print(test_results_df)

		

	# 	if len(test_results_df) > 0:
	# 		passed_test_results_df = test_results_df[test_results_df['summary_result'] == 'pass']
	# 		failed_test_results_df = test_results_df[test_results_df['summary_result'] == 'fail']
			
	# 	else:
	# 		passed_test_results_df = {}
	# 		failed_test_results_df = {}

	# 	my_expander = st.expander(label='Passed Every Test', expanded=True )
	# 	my_expander.dataframe(passed_test_results_df, 2000, 2000)	

	# 	my_expander = st.expander(label='Failed Every Test', expanded=False )
	# 	my_expander.dataframe(failed_test_results_df, 2000, 2000)	

	# 	my_expander = st.expander(label='Every Test Result', expanded=False )
	# 	my_expander.dataframe(test_results_df, 2000, 2000)	


	# 	# my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded )
	# 	# my_expander.dataframe(ticker_data_file, 2000, 2000)	