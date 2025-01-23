




def scope_page(scope):
	# ==========================================
	# variables for each page from the page list above

	scope.page = {}

	for page in scope.config['page_list']:
		scope.page[page] = {}
		
		scope.page[page]['search_results'] = {}
		scope.page[page]['worklist'] = []  			# formally known as scope.page[page]['ticker_list']
		scope.page[page]['worklist_long_desc'] = ['Show/Hide Data']
		scope.page[page]['loaded_ticker_list'] = []		# list of every ticker loaded by this particular page - saves checking later

		scope.page[page]['selectors'] = {
										'ticker'			: 'select a ticker',
										'tickers'			: [],
										'industries'		: [],
										'market'			: 'select market',
										'ticker_worklist'	: 'select a ticker',
										}
		# Settings are Changeable
		# Config is read only
		scope.page[page]['show'] = 	{
										'settings_charts':False,		# display the chart settings
										'settings_overlay':False,		# display the overlay settings
										'settings_trials':False,		# display the trial settings
										'settings_strategy':False,		# display the strategy settings
										'config_to_show':None,			# display the selected config
										'ticker_file':'Show/Hide Data',	# display the ticker files for the selected ticker
								}
		




		
