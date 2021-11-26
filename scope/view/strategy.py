import streamlit as st

from pages.view.three_cols import three_cols


def view_strategy(scope):
	st.subheader('Strategy Parameters')
	# TODO not sure what the final format of some of these objects should be

	three_cols( 'Strategy Name', scope.strategy_name, 'strategy_name' )
	three_cols( 'Print Header', scope.strategy_print_header, 'strategy_print_header' )

	col1,col2,col3 = st.columns([2,4,2])
	with col1: st.write('Price Columns')
	with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
	with col3: st.write('< strategy_price_columns >')
	
	three_cols( 'Print Count', scope.strategy_print_count, 'strategy_print_count' )
	three_cols( 'Build Header', scope.strategy_build_header, 'strategy_build_header' )
	three_cols( 'Header', scope.strategy_header, 'strategy_header' )
	three_cols( 'Print Line', scope.strategy_print_line, 'strategy_print_line' )
	
	col1,col2 = st.columns([6,2])
	with col1: st.write('Json Dicitionary')
	with col2: st.write('< strategy_json_dict >')
	st.write(scope.strategy_json_dict)

	col1,col2 = st.columns([6,2])
	with col1: st.write('Results Dataframe')
	with col2: st.write('< strategy_results >')
	st.dataframe(scope.strategy_results, 2000, 1200)