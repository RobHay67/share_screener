import yfinance as yf					# https://github.com/ranaroussi/yfinance

from y_finance.price_data.cache_yf import cache_yf_batch_data
from pages.messages.y_finance import render_download_message, render_download_complete_message
from tickers.schema import ticker_file_schema
from y_finance.schema import y_finance_schemas



def download_from_yahoo_finance(scope): 
	# download ticker data for a single or group of tickers
	# utilising the y_finance platform

	for batch_no, industry in enumerate(scope.download['yf_download_these_industries']):

		# cache batch download params
		scope.download['yf_batch_no'] = batch_no
		scope.download['yf_batch_industry'] = industry
		set_batch_params(scope)

		render_download_message(scope)		

		download_ticker_data(scope)

		format_yf_data(scope)	

		cache_yf_batch_data(scope)

	render_download_complete_message(scope)


def set_batch_params(scope):

	# convert an industry into a string of tickers acceptable to y_finance

	industry = scope.download['yf_batch_industry']
	
	if industry == 'random_tickers':
		# Selected specific tickers rather than by industry group					 
		page = scope.display_page
		ticker_list = scope.pages[page]['worklist']
	else:
		# selected a share market, industry or multiple industries
		industry_tickers = scope.ticker_index['df'][scope.ticker_index['df']['industry_group'] == industry ]
		ticker_list = industry_tickers.index.tolist()

	# Create a readable list of the tickers for Y_Finance
	y_finance_ticker_string = ""
	for ticker in ticker_list:
		if len(y_finance_ticker_string) != 0:
			y_finance_ticker_string += " "
		y_finance_ticker_string =  y_finance_ticker_string + ticker

	scope.download['yf_batch_ticker_string'] = y_finance_ticker_string

	# Set type of download for y_finance - single or multiple tickers
	if y_finance_ticker_string.count(' ') == 0:
		scope.download['yf_batch_type'] = 'single_ticker'
	else:
		scope.download['yf_batch_type'] = 'multiple_tickers'


def download_ticker_data(scope):

	# empty the temporary download data holder
	scope.download['yf_batch_data'] = {}
	scope.download['yf_batch_errors'] = {}
	downloaded_data = False

	if scope.download['yf_batch_type'] == 'single_ticker':
		# Single Ticker being downloaded
	
		yf_download = yf.download( 
									tickers=scope.download['yf_batch_ticker_string'], 
									period=scope.download['yf_period'], 
									interval='1d', 
									progress=True, 
									show_errors=False
									)			
		# manually add the ticker column as its missing
		yf_download['Ticker'] = scope.download['yf_batch_ticker_string']

		# print(yf_download)
		downloaded_data = True

	if scope.download['yf_batch_type'] == 'multiple_tickers':
		# Multiple Tickers being downloaded
			
		yf_download = yf.download( 
									tickers=scope.download['yf_batch_ticker_string'], 
									group_by = 'ticker', 				# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
									period=scope.download['yf_period'], 
									interval='1d', 
									progress=True, 
									threads=True, 						# threads : use threads for mass downloading? (True/False/Integer)
									show_errors=False 
									)
		# Sort out the column headers
		yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)

		downloaded_data = True

	if downloaded_data:
		scope.download['yf_batch_data'] = yf_download
		scope.download['yf_batch_errors'] = yf.shared._ERRORS


def format_yf_data(scope):
	
	# simple object reference
	schema = scope.download['yf_batch_type']
	yf_download = scope.download['yf_batch_data']

	# remove any index set during import - we will set the index later
	yf_download.reset_index(inplace=True)   

	for col_no in y_finance_schemas[schema]:
		provider_column_name = y_finance_schemas[schema][col_no]['col_name']
		if col_no < 50:                 	
			# its a column we are keeping - anything tagged with a key above 50 can be removed
			application_column_name = ticker_file_schema[col_no]['col_name']
			yf_download.rename(columns = { provider_column_name : application_column_name }, inplace = True)
		else:                           	
			# its a column we do not need so lets delete it
			del yf_download[provider_column_name]
	yf_download['volume'] = yf_download['volume'].fillna(0).astype(int)
	


