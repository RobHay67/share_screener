
import streamlit as st

from trials.results import trial_results



def render_trial_results(scope):

	st.write('**Trial Results**')

	trial_results_df = trial_results(scope)	

	if len(trial_results_df) > 0:
		passed_trial_results_df = trial_results_df[trial_results_df['summary_result'] == 'pass']
		failed_trial_results_df = trial_results_df[trial_results_df['summary_result'] == 'fail']
		
	else:
		passed_trial_results_df = {}
		failed_trial_results_df = {}

	col1,col2,col3 = st.columns([4,4,4])


	no_columns = len(trial_results_df.columns)

	pixel_width = 70 * no_columns
	pixel_row_height = 40

	with col1:
		no_passed = str(len(passed_trial_results_df))
		my_expander = st.expander(label='Passed Every Trial (' + no_passed + ' )', expanded=False )
		my_expander.dataframe(passed_trial_results_df, pixel_width, len(passed_trial_results_df)*pixel_row_height)	
	with col2:
		no_failed = str(len(failed_trial_results_df))
		my_expander = st.expander(label='Failed Every Trial (' + no_failed + ' )', expanded=False )
		my_expander.dataframe(failed_trial_results_df, pixel_width, len(failed_trial_results_df)*pixel_row_height)	
	with col3:
		no_trialed = str(len(trial_results_df))
		my_expander = st.expander(label='Every Trial Result (' + no_trialed + ' )', expanded=False )
		my_expander.dataframe(trial_results_df, pixel_width, len(trial_results_df)*pixel_row_height)	
















	# The original render trial results
	# TODO - delete after getting the trials working


	# def render_trial_results(scope):

	# 	st.write('**Trial Results**')

	# 	print('X'*66)

	# 	# App = scope.apps['display_app']

	# 	trial_results_df = scope.apps['trials']['df']
	# 					#   scope.apps['trials']['df'] = trial_results_df

	# 	# print('.'*77)
	# 	print('trial_results_df')
	# 	print(trial_results_df)

		

	# 	if len(trial_results_df) > 0:
	# 		passed_trial_results_df = trial_results_df[trial_results_df['summary_result'] == 'pass']
	# 		failed_trial_results_df = trial_results_df[trial_results_df['summary_result'] == 'fail']
			
	# 	else:
	# 		passed_trial_results_df = {}
	# 		failed_trial_results_df = {}

	# 	my_expander = st.expander(label='Passed Every Trial', expanded=True )
	# 	my_expander.dataframe(passed_trial_results_df, 2000, 2000)	

	# 	my_expander = st.expander(label='Failed Every Trial', expanded=False )
	# 	my_expander.dataframe(failed_trial_results_df, 2000, 2000)	

	# 	my_expander = st.expander(label='Every Trial Result', expanded=False )
	# 	my_expander.dataframe(trial_results_df, 2000, 2000)	


	# 	# my_expander = st.expander(label=(ticker+' ( ' + no_of_rows + ' )'), expanded=render_expanded )
	# 	# my_expander.dataframe(ticker_data_file, 2000, 2000)	