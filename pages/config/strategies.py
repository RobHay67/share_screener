import streamlit as st
from pages.config.three_cols import three_cols


def render_strategies(scope):

	st.subheader('Strategy Settings')
	three_cols( 'Strategy Settings stored in', {}, "scope.strategy", widget_type='string' )

	st.write('---')	
	three_cols( 'Strategy Name', scope.strategy['name'], 'scope.strategy.name' )
	three_cols( 'Price Columns', scope.strategy['price_columns'], 'scope.strategy.price_columns' )
	three_cols( 'JSON Dictionary', scope.strategy['json_dict'], 'scope.strategy_json_dict' )
	three_cols( 'Results Dataframe', scope.strategy['results'], 'scope.strategy.results' )
	three_cols( 'Print Header', scope.strategy['print_header'], 'scope.strategy.print_header' )
	three_cols( 'Header - Build', scope.strategy['header']['build'], 'scope.strategy.header.build' )
	three_cols( 'Header - Rows ', scope.strategy['header']['rows'], 'scope.strategy.header.rows' )
	three_cols( 'Print - Count', scope.strategy['print']['count'], 'scope.strategy.print.count' )
	three_cols( 'Print - Line ', scope.strategy['print']['line'], 'scope.strategy.print.line' )
	
