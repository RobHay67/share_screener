from ticker.model.downloader import download_from_yahoo_finance
from ticker.model.combiner import combine_loaded_and_download_ticker_data
from pages.view.results import view_results
from ticker.model.save import save_tickers


def download_tickers(scope):

	page = scope.page_to_display

	download_from_yahoo_finance(scope)
	view_results(scope)

	combine_loaded_and_download_ticker_data(scope)
	view_results(scope)

	# check_share_data_for_missing_dates( scope )				# TODO Not Sure this is Required anymore

	save_tickers( scope )
	view_results(scope)

	# reset STATUS to prevent unnecesary updates
	scope.download_industries 					= [] 			# Reset for next download
	scope.pages[page]['refresh_analysis_df'] 	= True
	scope.pages[page]['refresh_chart_df'] 		= True




