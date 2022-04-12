
def audit_titles(line_1, line_2):
	print('-'*70)
	print(line_1)
	print(line_2)
	print('-'*70)

def audit_footer():
	print('-'*70)
	print('')



def audit_report(scope):

	audit_titles('TICKER_LIST list of tickers being utilised by page ', 'scope / pages / [page] / ticker_list ')
	for page in scope.pages['page_list']:
		print (page, 'ticker_list = ', scope.pages[page]['ticker_list'])
	audit_footer()

	# audit_titles('selected ticker from ticker dropdown list','scope / pages / [page] / selectors' )
	# for page in scope.pages['page_list']:
	# 	print (page, 'selectors.ticker = ', scope.pages[page]['selectors']['ticker'])
	# audit_footer()

	audit_titles('RENEW TICKER_DATA - Ticker data that needs to be renewed for this page', 'scope / pages / [page] / renew / ticker_data / [ticker] / status')
	for page in scope.pages['page_list']:
		print(page.upper(), 'Page')
		for ticker, status in scope.pages[page]['renew']['ticker_data'].items():
			print ( ticker, ' : ', status)
	audit_footer()

	# audit_titles('Expander (Col adding functions) data that needs to be re-run for this page', 'scope / pages / [page] / renew / expanders / [ticker] / [expander] / status')
	# for page in scope.pages['page_list']:
	# 	print(page.upper(), 'Page')
	# 	ticker_list = list(scope.pages[page]['renew']['expanders'].keys())	
	# 	for ticker in ticker_list:
	# 		print(ticker)
	# 		for expander, status in scope.pages[page]['renew']['expanders'][ticker].items():
	# 			print ( ''.ljust(10) + expander.ljust(20) + ' : ' + str(status) )


	# audit_titles('Ticker data that needs to be renewed for this page', 'scope / pages / [page] / renew / expanders / [ticker] / [expander] / status')
	# for page in scope.pages['page_list']:
	# 	print(page.upper(), 'Page')
	# 	ticker_list = list(scope.pages[page]['renew']['expanders'].keys())	
	# 			for ticker in ticker_list:


	audit_footer()
