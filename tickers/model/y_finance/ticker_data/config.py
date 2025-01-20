


def set_download_config(scope, ticker_download_list):
	determine_batch_type(scope, ticker_download_list)
	create_readable_string(scope, ticker_download_list)
	scope.yf['batch_data'] = {}
	scope.yf['batch_errors'] = {}
	


def determine_batch_type(scope, ticker_download_list):
	if len(ticker_download_list) == 1:
		scope.yf['batch_type'] = 'single_ticker'
	else:
		scope.yf['batch_type'] = 'multiple_tickers'


def create_readable_string(scope, ticker_download_list):

	# Create a readable list of the tickers for Y_Finance
	ticker_string_for_y_finance = ""
	for ticker in ticker_download_list:
		if len(ticker_string_for_y_finance) != 0:
			ticker_string_for_y_finance += ", "
		ticker_string_for_y_finance =  ticker_string_for_y_finance + ticker
	
	# cache for download function
	scope.yf['batch_ticker_string'] = ticker_string_for_y_finance







