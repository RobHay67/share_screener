
# from share_screener.pages.ticker_loader.buttons.ticker_file import ticker_file_button


def audit_titles(line_1, line_2):
	print('-'*70)
	print(line_1)
	print(line_2)
	print('-'*70)

def audit_footer():
	print('-'*70)
	print('')







def audit_replace_df_status(scope):

	tab1=10
	page=scope.pages['display_page']

	# All loaded Ticker Files
	ticker_list = scope.data['ticker_files'].keys()

	print('')
	print('')
	print('='*100)
	print('replace_dfs > status')
	print('page        >', page.upper())
	print('do the dfs need replacing ?')
	print('-'*100)
	print( 'ticker'.ljust(tab1), 'single'.ljust(tab1), 'intraday'.ljust(tab1), 'volume'.ljust(tab1), 'research'.ljust(tab1), 'screener'.ljust(tab1) )
	for ticker in sorted(ticker_list):
		single 		= str(scope.pages['single']['replace_dfs'][ticker])
		intraday 	= str(scope.pages['intraday']['replace_dfs'][ticker])
		volume 		= str(scope.pages['volume']['replace_dfs'][ticker])
		research 	= str(scope.pages['research']['replace_dfs'][ticker])
		screener 	= str(scope.pages['screener']['replace_dfs'][ticker])

		single_pad = '     ' if single 		== 'True' else '    '
		intraa_pad = '     ' if intraday 	== 'True' else '    '
		volumn_pad = '     ' if volume 		== 'True' else '    '
		resear_pad = '     ' if research 	== 'True' else '    '

		single   	= '\033[91m' + str(single) 		+ '\033[0m' if single == 'True' 	else  '\033[92m' + str(single) + '\033[0m'
		intraday 	= '\033[91m' + str(intraday) 	+ '\033[0m' if intraday == 'True' 	else  '\033[92m' + str(intraday) + '\033[0m'
		volume 		= '\033[91m' + str(volume) 		+ '\033[0m' if volume == 'True' 	else  '\033[92m' + str(volume) + '\033[0m'
		research 	= '\033[91m' + str(research) 	+ '\033[0m' if research == 'True' 	else  '\033[92m' + str(research) + '\033[0m'
		screener 	= '\033[91m' + str(screener) 	+ '\033[0m' if screener == 'True' 	else  '\033[92m' + str(screener) + '\033[0m'

			# print( len(single))


		print( ticker.ljust(tab1), single, single_pad, intraday, intraa_pad, volume, volumn_pad, research, resear_pad, screener )

	print('='*100)


	if page in scope.pages['page_list']:
		ticker_list = list(scope.pages[page]['replace_cols'].keys())

		tab1=20
		tab2=10

		# Construct the header line
		line = 'Column Adder'.ljust(tab1)
		for ticker in ticker_list:line += str(ticker).ljust(tab2)
		line_width = len(line)
		
		print('')
		print('='*line_width)
		print('replace_cols > status')
		print('page         >', page.upper())
		print('do the columns need replacing ?')
		print('-'*line_width)


		config_group = 'tests' if page == 'screener' else 'charts'
		col_adder_template = scope.pages['templates'][config_group].copy()

		list_of_col_adders = list(col_adder_template.keys())

		print(line)
		print('-'*line_width)
		for col_adder in list_of_col_adders:
			new_line = str(col_adder).ljust(tab1)
			
			for ticker in ticker_list:
				status = scope.pages[page]['replace_cols'][ticker][col_adder]
				# print(status)
				padding = '      ' if status == True else '     '

				status	= '\033[91m' + str(status) + '\033[0m' if status == True else  '\033[92m' + str(status) + '\033[0m'
				
				new_line += (status+padding).ljust(tab2)
			
			print(new_line)

	print('='*100)








