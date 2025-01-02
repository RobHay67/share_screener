import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_user_strategy_settings(scope):

	st.subheader('Strategy Settings for User')
	st.write(':red[This should end up as editable options like the charts and trials - this is an examples of what the fields might end up like]')
	three_cols( 'Strategy Settings stored in', {}, "scope.strategy", widget_type='string' )

	st.divider()	
	three_cols( 'Strategy Name', scope.strategy['name'], 'scope.strategy.name' )
	three_cols( 'Price Columns', scope.strategy['price_columns'], 'scope.strategy.price_columns' )
