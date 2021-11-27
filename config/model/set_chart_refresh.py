

def set_refresh_charts_for_all_pages(scope):
	for page in scope.pages.keys():
		print(page)
		scope.pages[page]['refresh_chart_df'] = True


