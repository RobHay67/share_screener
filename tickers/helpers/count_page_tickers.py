

def count_page_tickers(scope):
	page = scope.display['page']
	page_counter=0
	ticker_list = list(scope.tickers.keys())
	for ticker in ticker_list:
		if len(scope.tickers[ticker][page]['df']) != 0:
			page_counter+=1
	return page_counter