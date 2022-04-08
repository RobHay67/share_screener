from pages.view.title import render_page_title
from pages.view.title import render_page_title


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_intraday_page(scope):
	# render_page_title(scope, 'Intra Day Analysis', 'intraday')
	render_page_title(scope, 'Intra Day Analysis')

	ticker = scope.pages['intraday']['ticker_list'][0]

	if ticker in list(scope.data['ticker_files'].keys()):

		print('TODO render_intraday_page')

		


