import logging
from tickers.scope.model.scope_yf import scope_yf_config
from tickers.model.y_finance.ticker_data.config import set_download_config
from tickers.model.y_finance.ticker_data.single_ticker import single_ticker_downloader
from tickers.model.y_finance.ticker_data.multi_tickers import multiple_tickers_downloader
from tickers.model.y_finance.ticker_data.format import format_downloaded_ticker_data
from tickers.model.y_finance.ticker_data.append_to_yf_df import consolidate_downloaded_ticker_data
from tickers.model.y_finance.ticker_data.append_to_scope_tickers import append_downloaded_data_to_scope_tickers
from tickers.views.msg_download_complete import show_message_download_complete
from tickers.views.msg_no_tickers import no_tickers_selected


def download_ticker_data(scope):
	logging.debug("download_ticker_data")
	# utilising the y_finance platform

	page = scope.display['page']
	ticker_download_list = scope.page[page]['selected_tickers']
	
	scope_yf_config(scope)

	if len(ticker_download_list) > 0:
		# note : if the list becomes too large, we may need to break into batches again
		set_download_config(scope, ticker_download_list)
		
		match scope.yf['batch_type']:
			case 'single_ticker':single_ticker_downloader(scope)
			case 'multiple_tickers':multiple_tickers_downloader(scope)

		format_downloaded_ticker_data(scope)
		consolidate_downloaded_ticker_data(scope)
		append_downloaded_data_to_scope_tickers(scope, ticker_download_list)
		show_message_download_complete(scope, ticker_download_list)
	else:
		no_tickers_selected(scope)





