from analysis.views.titles import analysis_titles


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def analysis_intraday_page(scope):
	analysis_titles(scope, 'Intra Day Analysis', 'intraday')

	ticker = scope.pages['intraday']['ticker_list'][0]

	if ticker in list(scope.ticker_data_files.keys()):

		print('We are here')

		


