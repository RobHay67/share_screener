# trials_config - all config
# chart_list	- list of chart config keys
# active_list	- list of acttive chart config keys
# column_adders	-  dict of { chart : active_status } (includes active and inactive)
import logging

from charts.scope.schema import scope_charts_schema
from charts.scope.scope_chart_settings_for_user import scope_charts_for_users
from charts.helpers.active_list import build_chart_active_list
from charts.helpers.col_adders import build_charts_column_adder_template

def scope_charts(scope):
	logging.warning("scope_charts")
	scope.charts = {}
	scope_charts_schema(scope)
	scope_charts_for_users(scope)
	scope.charts['chart_list'] = list(scope.charts['schema'].keys())
	scope.charts['colours'] = ['blue','orange','green','red','LightSkyBlue','ForestGreen','SteelBlue','black', 'yellow']
	build_chart_active_list(scope)
	build_charts_column_adder_template(scope)



	








