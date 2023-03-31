

from ticker_index.schema import schema
from ticker_index.load import load_ticker_index_file



def scope_index_file(scope):

	scope.ticker_index = {}	

	scope.ticker_index['schema'] = schema
	scope.ticker_index['df'] = {}
	scope.ticker_index['df_downloaded'] = {}
	scope.ticker_index['render'] = {}
	scope.ticker_index['render']['industry_report'] = False
	
	# Messages to be rendered during ticker download and update process
	scope.ticker_index['render']['missing_ticker_index_file'] = False
	scope.ticker_index['render']['created_empty_ticker_index_file'] = False
	scope.ticker_index['render']['downloading_asx'] = False
	scope.ticker_index['render']['download_market_n_a'] = False
	scope.ticker_index['render']['download_success'] = False
	scope.ticker_index['render']['updating_ticker_index'] = False
	scope.ticker_index['render']['added_tickers'] = None			# Number of new tickers added during download
	scope.ticker_index['render']['saved_ticker_index'] = False
	scope.ticker_index['render']['non_editable_cols'] = []



	load_ticker_index_file(scope)







