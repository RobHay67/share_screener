import logging


def build_industry_dropdown_list(scope):
	logging.debug("build_industry_dropdown_list")
	list_of_industries = scope.ticker_index['df']['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.config['dropdowns']['industries'] = list_of_industries