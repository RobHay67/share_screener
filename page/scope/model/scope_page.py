import logging




def scope_page(scope):
	logging.warning("scope_page")

	scope.page = {}

	for page in scope.config['page_list']:
		scope.page[page] = {}
		
		scope.page[page]['list_loaded_tickers'] = []			# list of every ticker loaded by this particular page - saves checking later
		scope.page[page]['list_load_tickers'] = []				# as determined by the ticker selectors - and if it hasnt been previously loaded
		scope.page[page]['list_selected_tickers'] = []			# List of ticker(s) as chosen by the selectors for the page
		scope.page[page]['search_results'] = {}
		
		scope.page[page]['list_page_worklist'] = ['Show/Hide Data']
		scope.page[page]['replace_worklist'] = False			# flag to indicate that this job needs to be done
		
		scope.page[page]['external_link'] = 'None'				# store whatever the default external link button is

		scope.page[page]['selectors'] = {
										'ticker'			: None,			# select a single ticker (non screener page)
										'tickers'			: [],			# select a single or multiple tickers
										'industries'		: [],			# sleect every ticker in a particular industry
										'market'			: None, 		# select an entire market,
										}
		# Settings are Changeable
		# Config is read only
		scope.page[page]['show'] = 	{
										'charts'				:False,				# display the chart settings
										'overlays'				:False,				# display the overlay settings
										'trials'				:False,				# display the trial settings
										'strategy'				:False,				# display the strategy settings
										'active_trial_or_chart'	:False,				# display any active Trials or Charts
										'config'				:None,				# display the selected config
										'ticker_file'			:'Show/Hide Data',	# display the ticker files for the selected ticker
										'external_link'			:None,				# store whatever the default external link button is
								}
		




		
