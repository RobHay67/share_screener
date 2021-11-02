
import streamlit as st





# -----------------------------------------------------------------------------------------------------------------------------------
# Output Ticker Iteration to terminal
# -----------------------------------------------------------------------------------------------------------------------------------
def output_results_to_browser(scope, output=None, result=None, final_print=False, passed='', passed_2='', failed='' ):
	# I think what we do here is just build 3 list and save them

	if output == None:
		# this is the initial run so set all the defails
		# width_of_next_output = 0
		scope.result_passed=passed
		scope.result_passed_2=passed_2
		scope.result_failed=failed
		scope.result_passed_count = 0
		scope.result_passed_2_count = 0
		scope.result_failed_count = 0

	# Store the results
	if result=='passed':
		scope.result_passed = scope.result_passed + str(output) + ' '
		scope.result_passed_count +=1
	elif result=='passed_2':
		scope.result_passed_2 = scope.result_passed_2 + str(output) + ' '
		scope.result_passed_2_count +=1
	elif result=='failed':
		scope.result_failed = scope.result_failed + str(output) + ' '
		scope.result_failed_count +=1

	# print (scope.result_passed)
	if final_print: 
		scope.result_passed = scope.result_passed + ' < ( ' + str(scope.result_passed_count) + ' )'
		scope.result_passed_2 = scope.result_passed_2 + ' < ( ' + str(scope.result_passed_2_count) + ' )'
		scope.result_failed = scope.result_failed + ' < ( ' + str(scope.result_failed_count) + ' )'

		if scope.result_passed_count > 0: st.info(scope.result_passed)
		if scope.result_passed_2_count > 0: st.warning(scope.result_passed_2)

		# if len(scope.result_failed) != 0:
		if scope.result_failed_count > 0: st.error(scope.result_failed)

