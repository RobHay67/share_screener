import logging

from ticker_index.scope.model.schema import schema
from ticker_index.scope.model.load import load_ticker_index_file



def scope_ticker_index(scope):
	logging.debug("scope_ticker_index")
	scope.ticker_index = {}	

	scope.ticker_index['schema'] = schema
	scope.ticker_index['df'] = {}
	scope.ticker_index['download_cache'] = {}
	scope.ticker_index['save_edited_df'] = False				# Flag to save changes
	scope.ticker_index['editable_df_key'] = 1					# ??? to cancel changes (dont save)
	
	scope.ticker_index['show'] = {}
	scope.ticker_index['show']['ticker_index'] = True			# show the ticker index
	scope.ticker_index['show']['industry_report'] = False		# show the industry report
	scope.ticker_index['show']['editable_df'] = False			# show a ticker index that can be edited
	
	
	load_ticker_index_file(scope)







