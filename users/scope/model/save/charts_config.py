import logging


def save_charts_user_settings(scope):
	logging.debug("save_charts_user_settings")
	# Summarise the current CHARTS config for this user 
	excluded_attribute_list = ['function']

	chart_dict = {}

	for chart in scope.charts['chart_list']:
		chart_dict[chart] = {}

		# Save the overall active setting for the chart
		chart_dict[chart]['active'] = scope.charts['user_config'][chart]['active']

		# Save active_column attributes
		if 'active_columns' in scope.charts['user_config'][chart].keys():
			chart_dict[chart]['active_columns'] = scope.charts['user_config'][chart]['active_columns']

		# Save any column adding settings (i.e. selected column or duration)
		add_columns = scope.charts['user_config'][chart]['function']
		if add_columns != None:
			chart_dict[chart]['function'] = {}
			for attribute in add_columns.keys():
				# Save attributes (unless exluded)
				if attribute not in excluded_attribute_list:
					chart_dict[chart]['function'][attribute] = scope.charts['user_config'][chart]['function'][attribute]

		else:
			chart_dict[chart]['function'] = None	

	return chart_dict

