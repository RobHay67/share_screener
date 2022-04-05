from metrics.config import tests_config, trend_direction



def scope_tests(scope):

	scope.config['tests'] = {}

	scope.config['tests']['trends']	= trend_direction
	scope.config['tests']['test_list']	= list(tests_config.keys())

	for key, metrics in tests_config.items():
		scope.config['tests'][key] = metrics
	

