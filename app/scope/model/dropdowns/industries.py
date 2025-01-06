


def build_inductry_dropdown_list(scope):
	list_of_industries = scope.ticker_index['df']['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.pages['dropdowns']['industries'] = list_of_industries