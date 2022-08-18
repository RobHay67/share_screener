from tickers.download.y_finance import download_from_yahoo_finance
from tickers.combiner import combine_loaded_and_downloaded_ticker_data
from partials.messages.progress import render_progress_messages
from tickers.save import save_tickers
from tickers.status.download import reset_industry_groups


def download_tickers(scope):

	download_from_yahoo_finance(scope)
	render_progress_messages(scope)

	combine_loaded_and_downloaded_ticker_data(scope)
	render_progress_messages(scope)

	# check_share_data_for_missing_dates( scope )				# TODO Not Sure this is Required anymore

	save_tickers(scope)
	render_progress_messages(scope)

	# reset STATUS to prevent unnecesary updates
	reset_industry_groups(scope)




