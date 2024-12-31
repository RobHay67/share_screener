
def initilize_yf_config(scope, ticker_download_list):
	determine_batch_type(scope, ticker_download_list)
	create_readable_string(scope, ticker_download_list)


def determine_batch_type(scope, ticker_download_list):
	if len(ticker_download_list) == 1:
		scope.yf['batch_type'] = 'single_ticker'
	else:
		scope.yf['batch_type'] = 'multiple_tickers'


def create_readable_string(scope, ticker_download_list):

	# Create a readable list of the tickers for Y_Finance
	y_finance_ticker_string = ""
	for ticker in ticker_download_list:
		if len(y_finance_ticker_string) != 0:
			y_finance_ticker_string += " "
		y_finance_ticker_string =  y_finance_ticker_string + ticker
	scope.yf['batch_ticker_string'] = y_finance_ticker_string







