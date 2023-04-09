from y_finance.price_data.y_finance import download_from_yahoo_finance
from y_finance.price_data.combine import combine_cached_and_yf_data
from y_finance.config import reset_yf_download_config


def download_tickers(scope):

	download_from_yahoo_finance(scope)

	combine_cached_and_yf_data(scope)

	reset_yf_download_config(scope)





