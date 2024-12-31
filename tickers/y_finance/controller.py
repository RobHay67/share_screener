from tickers.y_finance.download.init_batch import initilize_yf_config
# from tickers.y_finance.download.init_batch import initilize_yf_config_new
from tickers.y_finance.download.controller import download_data_from_yf
from tickers.y_finance.download.format import format_downloaded_batch
# from tickers.y_finance.download.format import format_downloaded_batch_new
from tickers.y_finance.cache.batch_data import cache_batch_data
from tickers.y_finance.cache.ticker_data import cache_entire_download
from tickers.y_finance.scope_yf import scope_yf_config
from tickers.views.msg_download import render_message_download
from tickers.views.msg_download_complete import render_message_download_complete
from tickers.views.msg_no_tickers import no_tickers_selected


def download_ticker_data(scope):
	print('Running download_ticker_data')
	counter = 1
	print(counter)

	# download_from_yahoo_finance(scope)
	# download ticker data for a single or group of tickers
	# utilising the y_finance platform

	page = scope.pages['display']
	ticker_download_list = scope.pages[page]['worklist']

	if len(ticker_download_list) > 0:
		initilize_yf_config(scope, ticker_download_list)
		print('Finished initilize_yf_config')
		download_data_from_yf(scope)
		format_downloaded_batch(scope)

	# 	# Iterate through each industry (break up the download)
	# 	# for batch_no, industry in enumerate(scope.yf['download_these_industries']):
	# 	# 	initilize_yf_config(scope, batch_no, industry)
	# 	# 	render_message_download(scope)		
	# 	# 	download_data_from_yf(scope)
	# 	# 	format_downloaded_batch(scope)	
		cache_batch_data(scope)
		
		cache_entire_download(scope, ticker_download_list)
		render_message_download_complete(scope, ticker_download_list)
	# 	# scope_yf_config(scope)

	else:
		no_tickers_selected(scope)





