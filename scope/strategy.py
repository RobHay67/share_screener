

def scope_strategy(scope):
	# Strategy Params
	scope.strategy_name = 'None yet Selected', 
	scope.strategy_print_header = True
	scope.strategy_price_columns = ['open', 'high', 'low', 'close' ]
	scope.strategy_print_count = 0
	scope.strategy_build_header = True
	scope.strategy_header = {1:'', 2:'', 3:'', 4:''}
	scope.strategy_print_line = ''
	scope.strategy_json_dict = { "shares":{}, "columnNames":[] }
	scope.strategy_results = {}