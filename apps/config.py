from trials.config import trials_config
from charts.config import charts_config



def scope_apps(scope):

	scope.apps = {}
	base_config_apps(scope)
	scope.apps['button_for_scope'] = None
	scope.apps['app_list'] = ['chart', 'intraday', 'volume', 'research', 'screener', 'websites']
	
	# ==========================================
	# variables for each app from the app list above
	for app in scope.apps['app_list']:
		scope.apps[app] = {}
		scope.apps[app]['search_results'] = {}
		scope.apps[app]['worklist'] = []  # formally known as scope.apps[app]['ticker_list']
		scope.apps[app]['mined_tickers'] = []
		
		scope.apps[app]['selectors'] = {
										'ticker'	: 'select a ticker',
										'tickers'	: [],
										'industries': [],
										'market'	: 'select entire market', 
										}
		
		scope.apps[app]['render'] = 	{
										'tickers':False,
										'charts':False,
										'trials':False
								}


def base_config_apps(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.apps['row_limit'] = 100
	scope.apps['display_app'] = 'login'
