import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_strategy_config(scope):
	with st.expander("Strategy Configuration", expanded=False):
		st.write(':red[TODO > This is an example only and requires configuration]')
		three_cols( 'Strategy Config stored in', {}, "scope.strategy", widget_type='string' )

		st.divider()	
		three_cols( 'Strategy Name', scope.strategy['name'], 'scope.strategy.name' )
		three_cols( 'Price Columns', scope.strategy['price_columns'], 'scope.strategy.price_columns' )
		three_cols( 'JSON Dictionary', scope.strategy['json_dict'], 'scope.strategy_json_dict' )
		three_cols( 'Results Dataframe', scope.strategy['results'], 'scope.strategy.results' )
		three_cols( 'Print Header', scope.strategy['print_header'], 'scope.strategy.print_header' )
		three_cols( 'Header - Build', scope.strategy['header']['build'], 'scope.strategy.header.build' )
		three_cols( 'Header - Rows ', scope.strategy['header']['rows'], 'scope.strategy.header.rows' )
		three_cols( 'Print - Count', scope.strategy['print']['count'], 'scope.strategy.print.count' )
		three_cols( 'Print - Line ', scope.strategy['print']['line'], 'scope.strategy.print.line' )