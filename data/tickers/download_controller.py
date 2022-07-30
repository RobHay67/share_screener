from data.tickers.download import download_from_yahoo_finance
from data.tickers.combiner import combine_loaded_and_download_ticker_data
from apps.ticker_loader.messages import view_result
from data.tickers.save import save_tickers



def download_tickers(scope):

	page = scope.pages['display_page']

	download_from_yahoo_finance(scope)
	view_result(scope)

	combine_loaded_and_download_ticker_data(scope)
	view_result(scope)

	# check_share_data_for_missing_dates( scope )				# TODO Not Sure this is Required anymore

	save_tickers(scope)
	view_result(scope)

	# reset STATUS to prevent unnecesary updates
	scope.data['download']['industries'] = [] 								# Reset for next download




