
# from share_screener.pages.ticker_loader.buttons.ticker_file import ticker_file_button


def audit_titles(line_1, line_2):
	print('-'*70)
	print(line_1)
	print(line_2)
	print('-'*70)

def audit_footer():
	print('-'*70)
	print('')



def audit_report(scope):

	# audit_titles('TICKER_LIST list of tickers being utilised by page ', 'scope / pages / [page] / ticker_list ')
	# for page in scope.pages['page_list']:
	# 	print (page, 'ticker_list = ', scope.pages[page]['ticker_list'])
	# audit_footer()

	# audit_titles('selected ticker from ticker dropdown list','scope / pages / [page] / selectors' )
	# for page in scope.pages['page_list']:
	# 	print (page, 'selectors.ticker = ', scope.pages[page]['selectors']['ticker'])
	# audit_footer()

	# audit_titles('RENEW TICKER_DATA - Ticker data that needs to be renewed for this page', 'scope / pages / [page] / renew / ticker_data / [ticker] / status')
	# for page in scope.pages['page_list']:
	# 	print(page.upper(), 'Page')
	# 	for ticker, status in scope.pages[page]['tickers']['renew_df'].items():
	# 		print ( ticker, ' : ', status)
	# audit_footer()

	# audit_titles('col_adder (Col adding functions) data that needs to be re-run for this page', 'scope / pages / [page] / renew / column_adders / [ticker] / [col_adder] / status')
	# for page in scope.pages['page_list']:
	# 	print(page.upper(), 'Page')
	# 	ticker_list = list(scope.pages[page]['renew']['column_adders'].keys())	
	# 	for ticker in ticker_list:
	# 		print(ticker)
	# 		for col_adder, status in scope.pages[page]['renew']['column_adders'][ticker].items():
	# 			print ( ''.ljust(10) + col_adder.ljust(20) + ' : ' + str(status) )


	# audit_titles('Ticker data that needs to be renewed for this page', 'scope / pages / [page] / renew / column_adders / [ticker] / [col_adder] / status')
	# for page in scope.pages['page_list']:
	# 	print(page.upper(), 'Page')
	# 	ticker_list = list(scope.pages[page]['renew']['column_adders'].keys())	
	# 			for ticker in ticker_list:


	audit_footer()







def audit_replace_df_status(scope, message=None):

	tab1=10
	# All loaded Ticker Files
	ticker_list = scope.data['ticker_files'].keys()

	print('')
	print('')
	print('='*100)
	print('replace_df status ', message)
	print('-'*100)
	print( 'ticker'.ljust(tab1), 'single'.ljust(tab1), 'intraday'.ljust(tab1), 'volume'.ljust(tab1), 'research'.ljust(tab1), 'screener'.ljust(tab1) )
	for ticker in sorted(ticker_list):
		single 		= str(scope.pages['single']['replace_df'][ticker])
		intraday 	= str(scope.pages['intraday']['replace_df'][ticker])
		volume 		= str(scope.pages['volume']['replace_df'][ticker])
		research 	= str(scope.pages['research']['replace_df'][ticker])
		screener 	= str(scope.pages['screener']['replace_df'][ticker])

		single_pad = '     ' if single 		== 'True' else '    '
		intraa_pad = '     ' if intraday 	== 'True' else '    '
		volumn_pad = '     ' if volume 		== 'True' else '    '
		resear_pad = '     ' if research 	== 'True' else '    '

		single   	= '\033[91m' + str(single) 		+ '\033[0m' if single == 'True' 		else  '\033[92m' + str(single) + '\033[0m'
		intraday 	= '\033[91m' + str(intraday) 	+ '\033[0m' if intraday == 'True' 	else  '\033[92m' + str(intraday) + '\033[0m'
		volume 		= '\033[91m' + str(volume) 		+ '\033[0m' if volume == 'True' 		else  '\033[92m' + str(volume) + '\033[0m'
		research 	= '\033[91m' + str(research) 	+ '\033[0m' if research == 'True' 	else  '\033[92m' + str(research) + '\033[0m'
		screener 	= '\033[91m' + str(screener) 	+ '\033[0m' if screener == 'True' 	else  '\033[92m' + str(screener) + '\033[0m'

			# print( len(single))


		print( ticker.ljust(tab1), single, single_pad, intraday, intraa_pad, volume, volumn_pad, research, resear_pad, screener )

	print('='*100)

	# print(scope.pages['single']['dfs']['ANZ.AX'])







