import logging
from files.helpers.ticker_path import path_for_ticker_file
from tickers.model.missing.save import save_ticker_event

def save_ticker(scope, ticker):
	logging.warning("save_ticker")
	path_for_ticker_file(scope, ticker, 'save')

	saving_df = scope.tickers[ticker]['df'].copy()
	saving_df.to_csv( scope.files['paths']['ticker_data'], index=False )

	save_ticker_event(scope, ticker)


