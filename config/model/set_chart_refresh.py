

def set_refresh_charts_for_all_pages(scope):
	for page in scope.pages.keys():
		print(page)
		for ticker in scope.pages[page]['refresh_chart_df'].keys():
			print(ticker)
			scope.pages[page]['refresh_chart_df'][ticker] = True


