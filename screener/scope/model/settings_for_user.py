
from screener.scope.model.schema import trials_schema


def trial_settings_for_user(scope):
	# store the trial configuration dictionary (from below)
	scope.trials['user_config'] = {}
	for trial, configuration in trials_schema.items():
		scope.trials['user_config'][trial] = configuration.copy()



