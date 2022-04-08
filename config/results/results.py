

def store_result(scope, output=None, result=None, final_print=False, passed='', passed_2='', failed='' ):

	if output == None:
		# this is the initial run so set all the counts to zero
		scope.config['results']['passed']			= passed
		scope.config['results']['passed_2']		= passed_2
		scope.config['results']['failed']			= failed
		scope.config['results']['passed_count'] 	= 0
		scope.config['results']['passed_2_count'] = 0
		scope.config['results']['failed_count'] 	= 0

	# Store the results
	if result=='passed':
		scope.config['results']['passed'] = scope.config['results']['passed'] + str(output) + ' '
		scope.config['results']['passed_count'] +=1
	elif result=='passed_2':
		scope.config['results']['passed_2'] = scope.config['results']['passed_2'] + str(output) + ' '
		scope.config['results']['passed_2_count'] +=1
	elif result=='failed':
		scope.config['results']['failed'] = scope.config['results']['failed'] + str(output) + ' '
		scope.config['results']['failed_count'] +=1

	if final_print: 
		scope.config['results']['passed']   = scope.config['results']['passed']   + ' < ( ' + str(scope.config['results']['passed_count']) + ' )'
		scope.config['results']['passed_2'] = scope.config['results']['passed_2'] + ' < ( ' + str(scope.config['results']['passed_2_count']) + ' )'
		scope.config['results']['failed']   = scope.config['results']['failed']   + ' < ( ' + str(scope.config['results']['failed_count']) + ' )'

		# if scope.config['results']['passed_count'] > 0: st.info(scope.config['results']['passed'])
		# if scope.config['results']['passed_2_count'] > 0: st.warning(scope.config['results']['passed_2'])
		# if scope.config['results']['failed_count'] > 0: st.error(scope.config['results']['failed'])