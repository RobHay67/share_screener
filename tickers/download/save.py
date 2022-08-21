
from files.path import path_for_ticker_file
from tickers.events.save_ticker import set_save_ticker_status

def save_ticker(scope, ticker):

	path_for_ticker_file(scope, ticker)

	saving_df = scope.tickers[ticker]['df'].copy()
	saving_df.to_csv( scope.files['paths']['ticker_data'], index=False )

	set_save_ticker_status(scope, ticker)


