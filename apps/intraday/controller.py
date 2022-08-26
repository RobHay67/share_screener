from partials.app_header.controller import render_app_header

from partials.ticker_search.search_results import render_search_results
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_intraday_page(scope):

	app = scope.apps['display_app']

	render_app_header(scope, 'Intra Day Analysis')

	if len(scope.apps[app]['search_results']) == 0:

		ticker = scope.apps[app]['selectors']['ticker']

		if ticker != 'select a ticker' :		
			
			if ticker in list(scope.tickers.keys()):

				print('TODO render_intraday_page')
		
	else:
		render_search_results(scope)


