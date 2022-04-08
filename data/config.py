


from data.index.config import scope_index
from data.tickers.config import scope_tickers
from data.tickers.config import scope_download

def scope_data(scope):

	scope.data = {}

	# if scope.initial_load:					# This will only run one time after the initial load has occured
	scope_index(scope)
	scope.initial_load = False			# Prevent session_state from re-running during its use

	scope_tickers(scope)

	scope_download(scope)