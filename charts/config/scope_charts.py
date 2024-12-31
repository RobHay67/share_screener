# trials_config - all config
# chart_list	- list of chart config keys
# active_list	- list of acttive chart config keys
# column_adders	-  dict of { chart : active_status } (includes active and inactive)

from charts.config.active_list import chart_active_list

from charts.config.schema import charts_config
from charts.config.col_adders import chart_column_adders


def scope_charts(scope):
	scope.charts = {}
	base_config_charts(scope)
	scope.charts['chart_list'] = list(charts_config.keys())
	scope.charts['colours'] = ['blue','orange','green','red','LightSkyBlue','ForestGreen','SteelBlue','black', 'yellow']
	
	chart_active_list(scope)

	chart_column_adders(scope)


def base_config_charts(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.charts['primary_height'] = 500
	scope.charts['total_height'] = scope.charts['primary_height']

	# store the chart configuration dictionary (from below)
	scope.charts['config'] = {}
	for chart, config in charts_config.items():
		scope.charts['config'][chart] = config.copy()
	








