import streamlit as st


from system.reports import render_3_columns





def scope_results(scope):
	# Results - for batch processing of multiple tickers
	scope.results = { 'passed':'', 'passed_2':'', 'failed':'', 'passed_count':0, 'passed_2_count':0, 'failed_count':0 }

def render_results(scope):
	st.subheader('Results from Most Recent Batch Process')
	st.markdown("""---""")
	st.subheader('Result Parameters')
	render_3_columns( 'Result Passed', scope.results['passed'], "result['passed']" )
	render_3_columns( 'Result Passed_2', scope.results['passed_2'], "result['passed_2']" )
	render_3_columns( 'Result Failed', scope.results['failed'], "result['failed']" )
	render_3_columns( 'Count Passed', scope.results['passed_count'], "result['passed_count']" )
	render_3_columns( 'Count Passed_2', scope.results['passed_2_count'], "result['passed_2_count']" )
	render_3_columns( 'Count Failed', scope.results['failed_count'], "result['failed_count']" )
	
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





