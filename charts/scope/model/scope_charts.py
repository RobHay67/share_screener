# trials_config - all config
# chart_list	- list of chart config keys
# active_list	- list of acttive chart config keys
# column_adders	-  dict of { chart : active_status } (includes active and inactive)


from charts.scope.model.schema import scope_charts_schema
from charts.scope.model.chart_settings_for_user import chart_settings_for_user
from charts.helpers.active_list import chart_active_list
from charts.helpers.col_adders import chart_column_adders

def scope_charts(scope):
	scope.charts = {}
	scope_charts_schema(scope)
	chart_settings_for_user(scope)
	scope.charts['chart_list'] = list(scope.charts['schema'].keys())
	scope.charts['colours'] = ['blue','orange','green','red','LightSkyBlue','ForestGreen','SteelBlue','black', 'yellow']
	chart_active_list(scope)
	chart_column_adders(scope)



	








