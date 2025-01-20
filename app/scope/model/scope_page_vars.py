




def scope_page_variables(scope):
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
		
		scope.page[page]['render'] = 	{
										'ticker_file':'Show/Hide Data',	# display the ticker files
										'page_config':False,			# display the application config
										'chart_settings':False,			# display the chart settings
										'overlay_settings':False,		# display the overlay settings
										'trial_settings':False,			# display the trial settings
										'strategy':False,				# display the strategy settings
										'ticker_config':False,			# display the ticker config
								}
		




		
