




def scope_page(scope):
	# ==========================================
	# variables for each page from the page list above

	scope.page = {}

	for page in scope.config['page_list']:
		scope.page[page] = {}
		
		scope.page[page]['search_results'] = {}
		scope.page[page]['selected_tickers'] = []  			# formally known as scope.page[page]['ticker_list']
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
										'charts'		:False,				# display the chart settings
										'overlays'		:False,				# display the overlay settings
										'trials'		:False,				# display the trial settings
										'strategy'		:False,				# display the strategy settings
										'config'		:None,				# display the selected config
										'ticker_file'	:'Show/Hide Data',	# display the ticker files for the selected ticker
								}
		




		
