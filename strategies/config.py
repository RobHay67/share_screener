import streamlit as st
from config.progress.three_cols import three_cols

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




def view_strategy(scope):
	st.subheader('Strategy Parameters')
	three_cols( 'Strategy Name', scope.strategy['name'], 'scope.strategy.name' )
	three_cols( 'Price Columns', scope.strategy['price_columns'], 'scope.strategy.price_columns' )
	three_cols( 'JSON Dictionary', scope.strategy['json_dict'], 'scope.strategy_json_dict' )
	three_cols( 'Results Dataframe', scope.strategy['results'], 'scope.strategy.results' )
	three_cols( 'Print Header', scope.strategy['print_header'], 'scope.strategy.print_header' )
	three_cols( 'Header - Build', scope.strategy['header']['build'], 'scope.strategy.header.build' )
	three_cols( 'Header - Rows ', scope.strategy['header']['rows'], 'scope.strategy.header.rows' )
	three_cols( 'Print - Count', scope.strategy['print']['count'], 'scope.strategy.print.count' )
	three_cols( 'Print - Line ', scope.strategy['print']['line'], 'scope.strategy.print.line' )
	
