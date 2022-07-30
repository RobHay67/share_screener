

# -----------------------------------------------------------------------------------------------------------------------------------
# Store Results
# -----------------------------------------------------------------------------------------------------------------------------------

def cache_progress(scope, output=None, result=None, final_print=False, passed='', passed_2='', failed='' ):

	if output == None:
		# this is the initial run so set all the counts to zero
		scope.progress['passed']			= passed
		scope.progress['passed_2']		= passed_2
		scope.progress['failed']			= failed
		scope.progress['passed_count'] 	= 0
		scope.progress['passed_2_count'] = 0
		scope.progress['failed_count'] 	= 0

	# Store the results
	if result=='passed':
		scope.progress['passed'] = scope.progress['passed'] + str(output) + ' '
		scope.progress['passed_count'] +=1
	elif result=='passed_2':
		scope.progress['passed_2'] = scope.progress['passed_2'] + str(output) + ' '
		scope.progress['passed_2_count'] +=1
	elif result=='failed':
		scope.progress['failed'] = scope.progress['failed'] + str(output) + ' '
		scope.progress['failed_count'] +=1

	if final_print: 
		scope.progress['passed']   = scope.progress['passed']   + ' < ( ' + str(scope.progress['passed_count']) + ' )'
		scope.progress['passed_2'] = scope.progress['passed_2'] + ' < ( ' + str(scope.progress['passed_2_count']) + ' )'
		scope.progress['failed']   = scope.progress['failed']   + ' < ( ' + str(scope.progress['failed_count']) + ' )'
