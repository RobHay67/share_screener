
import streamlit as st

# -----------------------------------------------------------------------------------------------------------------------------------
# Output Ticker Iteration to Browser
# -----------------------------------------------------------------------------------------------------------------------------------
def results(scope, output=None, result=None, final_print=False, passed='', passed_2='', failed='' ):
	# I think what we do here is just build 3 list and save them

	if output == None:
		# this is the initial run so set all the defails
		scope.results['passed']=passed
		scope.results['passed_2']=passed_2
		scope.results['failed']=failed
		scope.results['passed_count'] = 0
		scope.results['passed_2_count'] = 0
		scope.results['failed_count'] = 0

	# Store the results
	if result=='passed':
		scope.results['passed'] = scope.results['passed'] + str(output) + ' '
		scope.results['passed_count'] +=1
	elif result=='passed_2':
		scope.results['passed_2'] = scope.results['passed_2'] + str(output) + ' '
		scope.results['passed_2_count'] +=1
	elif result=='failed':
		scope.results['failed'] = scope.results['failed'] + str(output) + ' '
		scope.results['failed_count'] +=1

	if final_print: 
		scope.results['passed']   = scope.results['passed']   + ' < ( ' + str(scope.results['passed_count']) + ' )'
		scope.results['passed_2'] = scope.results['passed_2'] + ' < ( ' + str(scope.results['passed_2_count']) + ' )'
		scope.results['failed']   = scope.results['failed']   + ' < ( ' + str(scope.results['failed_count']) + ' )'

		if scope.results['passed_count'] > 0: st.info(scope.results['passed'])
		if scope.results['passed_2_count'] > 0: st.warning(scope.results['passed_2'])
		if scope.results['failed_count'] > 0: st.error(scope.results['failed'])


