from tickers.download import download_from_yahoo_finance
from tickers.combiner import combine_loaded_and_download_ticker_data
from partials.ticker_loader.messages import render_messages
from tickers.save import save_tickers



def download_tickers(scope):

	app = scope.apps['display_app']

	download_from_yahoo_finance(scope)
	render_messages(scope)

	combine_loaded_and_download_ticker_data(scope)
	render_messages(scope)

	# check_share_data_for_missing_dates( scope )				# TODO Not Sure this is Required anymore

	save_tickers(scope)
	render_messages(scope)

	# reset STATUS to prevent unnecesary updates
	scope.download['industries'] = [] 								# Reset for next download




