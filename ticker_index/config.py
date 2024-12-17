

from ticker_index.schema import schema
from ticker_index.load import load_ticker_index_file



def scope_index_file(scope):

	scope.ticker_index = {}	

	scope.ticker_index['schema'] = schema
	scope.ticker_index['df'] = {}
	scope.ticker_index['df_downloaded'] = {}
	scope.ticker_index['render'] = {}
	scope.ticker_index['render']['industry_report'] = False
	scope.ticker_index['render']['save_edited_df'] = False
	scope.ticker_index['render']['editable_df'] = False
	scope.ticker_index['render']['editable_df_key'] = 1
	
	
	
	load_ticker_index_file(scope)







