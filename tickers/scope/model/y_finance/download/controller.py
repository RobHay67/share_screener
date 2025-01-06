from tickers.scope.model.y_finance.download.single_ticker import single_ticker_downloader
from tickers.scope.model.y_finance.download.multi_tickers import multiple_tickers_downloader


def download_data_from_yf(scope):

	batch_type = scope.yf['batch_type']
	scope.yf['batch_data'] = {}

	if batch_type == 'single_ticker':
		single_ticker_downloader(scope)		

	if batch_type == 'multiple_tickers':
		multiple_tickers_downloader(scope)	
