from trials.config import trials_config
from charts.config import charts_config



def scope_apps(scope):

	scope.apps = {}

	scope.apps['row_limit'] = 100
	scope.apps['button_for_scope'] = None
	scope.apps['display_app'] = 'login'
	scope.apps['app_list'] = ['single', 'intraday', 'volume', 'research', 'screener']
	
	# ==========================================
	# variables for each app from the app list above
	for app in scope.apps['app_list']:
		scope.apps[app] = {}
		scope.apps[app]['search_results'] = {}
		scope.apps[app]['selected_tickers'] = []  # formally known as scope.apps[app]['ticker_list']
		scope.apps[app]['mined_tickers'] = []
		
		scope.apps[app]['selectors'] = {
											'market'	: 'select entire market', 
											'industries': [],
											'tickers'	: [],
											'ticker'	: 'select a ticker',
											}



