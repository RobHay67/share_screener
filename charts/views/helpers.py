import streamlit as st



def edit_active(scope, chart ):

	display_name =  '' + scope.charts[chart]['name']
	
	previous_active_status = scope.charts[chart]['active']
	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								)
	scope.charts[chart]['active'] = new_active_status

	if new_active_status != previous_active_status : chart_df_may_need_a_refresh(scope)

	
def edit_number(scope, chart, column ):
	
	display_name = scope.charts[chart]['name']
	column_name = column.capitalize()
	
	previous_period = int(scope.charts[chart]['data_cols'][column])
	input_period_no = st.number_input(
										# column_name,
										label=(column_name + ' for ' + display_name), 
										min_value=0, 
										value=previous_period,
										key=display_name
										)  
	scope.charts[chart]['data_cols'][column] = input_period_no

	if input_period_no != previous_period : chart_df_may_need_a_refresh(scope)

	
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

	if selected_column != previous_column : chart_df_may_need_a_refresh(scope)
	
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

	if selected_column != previous_column : chart_df_may_need_a_refresh(scope)
	
def edit_colour(scope, chart ):
	
	display_name = scope.charts[chart]['name']
	
	previous_colour = scope.charts[chart]['plot']['colour']

	selected_colour = st.selectbox ( 
									label=('Colour for ' + display_name), 
									options=scope.chart_colours,
									index=scope.chart_colours.index(previous_colour), 
									key=chart,
									) 
	scope.charts[chart]['plot']['colour'] = selected_colour

	# does not require a refresh_chart_df to be set to Trueh




def chart_df_may_need_a_refresh(scope):
	for page in scope.selected.keys():
		print(page)
		scope.selected[page]['refresh_chart_df'] = True