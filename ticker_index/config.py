

from ticker_index.schema import schema
from ticker_index.load import load_ticker_index_file



def scope_index_file(scope):

	scope.ticker_index = {}	

	scope.ticker_index['schema'] = schema
	scope.ticker_index['df'] = {}
	scope.ticker_index['df_downloaded'] = {}
	scope.ticker_index['render'] = {}
	scope.ticker_index['render']['industry_report'] = False
	
	load_ticker_index_file(scope)







