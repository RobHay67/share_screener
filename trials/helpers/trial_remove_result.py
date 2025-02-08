import logging


def remove_trial_result_column(scope, ticker, schema_key):
	logging.warning("remove_trial_result_column")
	ticker_df = scope.tickers[ticker]['screener']['df']
	if schema_key in ticker_df:
		del ticker_df[schema_key]