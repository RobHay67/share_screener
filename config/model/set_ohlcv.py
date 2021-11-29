import streamlit as st


from config.model.set_chart_refresh import set_refresh_charts_for_all_pages


def edit_ohlcv(scope, chart ):
	
	display_name = scope.charts[chart]['name']
	
	previous_column = scope.charts[chart]['data_cols']['column']
	selected_column = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_ohlcv_columns,
									index=scope.dropdown_ohlcv_columns.index(previous_column), 
									key=chart,
									) 
	scope.charts[chart]['data_cols']['column'] = selected_column

	if selected_column != previous_column : 
		set_refresh_charts_for_all_pages(scope)
	
def edit_price(scope, chart ):
	
	display_name = scope.charts[chart]['name']
	
	previous_column = scope.charts[chart]['data_cols']['column']
	selected_column = st.selectbox ( 
									label=('Column for ' + display_name), 
									options=scope.dropdown_price_columns,
									index=scope.dropdown_price_columns.index(previous_column), 
									key=chart,
									) 
	scope.charts[chart]['data_cols']['column'] = selected_column

	if selected_column != previous_column : 
		set_refresh_charts_for_all_pages(scope)


