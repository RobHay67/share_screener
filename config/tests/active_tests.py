





def scope_active_test_list(scope):
	active_test_list = []
	
	for test in scope.config['tests']['test_list']:	
		if scope.config['tests'][test]['active'] == True:
			active_test_list.append(test)

	return active_test_list


