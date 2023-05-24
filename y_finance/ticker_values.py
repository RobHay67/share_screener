from y_finance.values.batch import scope_batch_config
from pages.messages.y_finance import render_download_message, render_download_complete_message
from y_finance.values.download import download_ticker_data
from y_finance.values.format import format_downloaded_batch
from y_finance.values.cache import cache_batch_data
from y_finance.values.cache import cache_entire_download
from y_finance.config import scope_yf_config


def download_ticker_values(scope):

	# download_from_yahoo_finance(scope)
	# download ticker data for a single or group of tickers
	# utilising the y_finance platform

	for batch_no, industry in enumerate(scope.yf['download_these_industries']):

		scope_batch_config(scope, batch_no, industry)

		render_download_message(scope)		

		download_ticker_data(scope)

		format_downloaded_batch(scope)	

		cache_batch_data(scope)

	render_download_complete_message(scope)

	cache_entire_download(scope)

	scope_yf_config(scope)





