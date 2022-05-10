

from config.tests.config import trend_direction, tests_config




def scope_tests(scope):

	scope.config['tests'] = {}

	scope.config['tests']['trends']	= trend_direction
	scope.config['tests']['test_list']	= list(tests_config.keys())

	for test, config in tests_config.items():
		scope.config['tests'][test] = config


