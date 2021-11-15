import streamlit as st

from system.view import view_3_columns

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


def view_strategy(scope):
	st.subheader('Strategy Parameters')
	# TODO not sure what the final format of some of these objects should be

	view_3_columns( 'Strategy Name', scope.strategy_name, 'strategy_name' )
	view_3_columns( 'Print Header', scope.strategy_print_header, 'strategy_print_header' )

	col1,col2,col3 = st.columns([2,4,2])
	with col1: st.write('Price Columns')
	with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
	with col3: st.write('< strategy_price_columns >')
	
	view_3_columns( 'Print Count', scope.strategy_print_count, 'strategy_print_count' )
	view_3_columns( 'Build Header', scope.strategy_build_header, 'strategy_build_header' )
	view_3_columns( 'Header', scope.strategy_header, 'strategy_header' )
	view_3_columns( 'Print Line', scope.strategy_print_line, 'strategy_print_line' )
	
	col1,col2 = st.columns([6,2])
	with col1: st.write('Json Dicitionary')
	with col2: st.write('< strategy_json_dict >')
	st.write(scope.strategy_json_dict)

	col1,col2 = st.columns([6,2])
	with col1: st.write('Results Dataframe')
	with col2: st.write('< strategy_results >')
	st.dataframe(scope.strategy_results, 2000, 1200)