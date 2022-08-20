
from files.path import path_for_ticker_file


def save_ticker(scope, ticker):

	path_for_ticker_file(scope, ticker)

	saving_df = scope.tickers[ticker]['df'].copy()
	saving_df.to_csv( scope.files['paths']['ticker_data'], index=False )



