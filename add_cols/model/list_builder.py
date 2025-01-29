


def create_list_of_tickers_to_add_columns(scope, page):

	ticker_list = []

	for ticker in scope.page[page]['worklist']:
		# Ensure ticker data available otherwise
		# function will fail on missing columns
		if ticker in list(scope.tickers.keys()):
			status_add_ticker = False
			if scope.tickers[ticker][page]['replace_df']:
				status_add_ticker = True
			
			if True in scope.tickers[ticker][page]['replace_column_adder'].values():
				status_add_ticker = True

			# iterate through list 
			print(scope.tickers[ticker][page]['replace_column_adder'])


			if status_add_ticker:
				ticker_list.append(ticker)

	return ticker_list


