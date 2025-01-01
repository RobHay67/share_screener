# trials_config - all config
# chart_list	- list of chart config keys
# active_list	- list of acttive chart config keys
# column_adders	-  dict of { chart : active_status } (includes active and inactive)

from charts.config.active_list import chart_active_list

from charts.config.schema import charts_config
from charts.config.col_adders import chart_column_adders
from charts.config.user_config import user_config_charts

def scope_charts(scope):
	scope.charts = {}
	user_config_charts(scope)
	scope.charts['chart_list'] = list(charts_config.keys())
	scope.charts['colours'] = ['blue','orange','green','red','LightSkyBlue','ForestGreen','SteelBlue','black', 'yellow']
	
	chart_active_list(scope)

	chart_column_adders(scope)



	








