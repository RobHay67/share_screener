
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

import streamlit as st

from pages.view.three_cols import three_cols


def view_strategy(scope):
	st.subheader('Strategy Parameters')
	# TODO not sure what the final format of some of these objects should be

	three_cols( 'Strategy Name', scope.strategy['name'], 'strategy_name' )
	three_cols( 'Print Header', scope.strategy['print_header'], 'strategy_print_header' )

	col1,col2,col3 = st.columns([2,4,2])
	with col1: st.write('Price Columns')
	with col2: st.dataframe(scope.strategy['price_columns'], 100, 200)
	with col3: st.write('< strategy_price_columns >')
	
	three_cols( 'Print Count', scope.strategy['print']['count'], 'strategy_print_count' )
	three_cols( 'Build Header', scope.strategy['header']['build'], 'strategy_build_header' )
	three_cols( 'Header', scope.strategy['header']['rows'], 'strategy_header' )
	three_cols( 'Print Line', scope.strategy['print']['line'], 'strategy_print_line' )
	
	col1,col2 = st.columns([6,2])
	with col1: st.write('Json Dicitionary')
	with col2: st.write('< strategy_json_dict >')
	st.write(scope.strategy['json_dict'])

	col1,col2 = st.columns([6,2])
	with col1: st.write('Results Dataframe')
	with col2: st.write('< strategy_results >')
	st.dataframe(scope.strategy['results'], 2000, 1200)