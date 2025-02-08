import logging
from ticker_index.scope.model.schema import scope_ticker_index_schema
from ticker_index.scope.model.load import load_ticker_index_file
from ticker_index.scope.model.helpers.csv_dates import scope_ticker_index_csv_dates
from ticker_index.scope.model.helpers.csv_dtypes import scope_ticker_index_csv_dtypes
from ticker_index.scope.model.helpers.data_types import scope_ticker_index_data_types
from ticker_index.scope.model.helpers.default_values import scope_ticker_index_default_values
from ticker_index.scope.model.helpers.editable_columns import scope_ticker_index_editable_columns
from ticker_index.scope.model.helpers.uneditable_columns import scope_ticker_index_uneditable_columns

def scope_ticker_index(scope):
	logging.warning("scope_ticker_index")
	scope.ticker_index = {}	

	scope_ticker_index_schema(scope)
	scope.ticker_index['df'] = {}
	scope.ticker_index['download_cache'] = {}
	scope.ticker_index['save_edited_df'] = False				# Flag to save changes
	scope.ticker_index['editable_df_key'] = 1					# ??? to cancel changes (dont save)
	
	scope.ticker_index['show'] = {}
	scope.ticker_index['show']['ticker_index'] = True			# show the ticker index
	scope.ticker_index['show']['industry_report'] = False		# show the industry report
	scope.ticker_index['show']['editable_df'] = False			# show a ticker index that can be edited
	
	scope.ticker_index['lists'] = {}
	scope_ticker_index_csv_dates(scope)
	scope_ticker_index_csv_dtypes(scope)
	scope_ticker_index_data_types(scope)
	scope_ticker_index_default_values(scope)
	scope_ticker_index_editable_columns(scope)
	scope_ticker_index_uneditable_columns(scope)

	load_ticker_index_file(scope)







