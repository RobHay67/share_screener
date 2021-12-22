from pages.view.analysis_title import analysis_titles
from pages.view.analysis_title import analysis_titles


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_intraday_page(scope):
	# analysis_titles(scope, 'Intra Day Analysis', 'intraday')
	analysis_titles(scope, 'Intra Day Analysis')

	ticker = scope.pages['intraday']['ticker_list'][0]

	if ticker in list(scope.ticker_data_files.keys()):

		print('We are here')

		


