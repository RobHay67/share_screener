import streamlit as st


def scope_strategy(scope):
	# Strategy Params

	scope.strategy = {}

	scope.strategy['name'] = 'None yet Selected', 
	scope.strategy['price_columns'] = ['open', 'high', 'low', 'close' ]
	scope.strategy['json_dict'] = { "shares":{}, "columnNames":[] }
	scope.strategy['results'] = {}
	scope.strategy['print_header'] = True

	scope.strategy['header'] = {}
	scope.strategy['header']['build'] = True
	scope.strategy['header']['rows'] = {1:'', 2:'', 3:'', 4:''}

	scope.strategy['print'] = {}
	scope.strategy['print']['count'] = 0
	scope.strategy['print']['line'] = ''




