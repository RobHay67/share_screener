import time  


from charts.config import scope_chart
from results.config import scope_results
from screener.config import scope_tests


def scope_config(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'DDT - Data Driven Trading'
	scope.config['project_start_time'] = time.time()


	# System Wide Variables
	scope.config['share_market'] = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere

	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['update_dropdowns'] = False		# Intially set to false, the loading or refreshing of the 
																# share index file has resposibility to modify this, but can
																# only do this after loading the share index file

	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['ohlcv_columns'] 	= ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns '] = ['open', 'high', 'low', 'close' 		   ]	


	scope.config['tests'] = {}
	scope_tests(scope)


	scope.config['charts'] = {}
	scope_chart(scope)


	scope.config['results'] = {}
	scope_results(scope)
