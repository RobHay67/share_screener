import plotly.graph_objects as go
from plotly.subplots import make_subplots


import streamlit as st


from analysis.charts.candlestick import plot_candlestick







def render_selected_charts(scope, ticker):
	
	# Default Values for start of the run
	no_of_charts = 0
	relative_row_heights = []
	col_no = 1
	chart_render_list = []

	# any measures (SMA or EMA) should have been added at this stage, we just need to know we need to render them
	# print(scope.selected[scope.display_page]['plot_df'])

	plot_df = scope.selected[scope.display_page]['plot_df'][ticker]


	# print(plot_df)

	# TODO looks like we add a trace for any overlays to the charts after rendering the chart - where the hell do we store this info
	# TODO height may need to end up be some relative proportion that is then fed into an over all height or number of charts to work out the actual value

	# charts_schema = {
	# 				'candlestick'	:{'title':'Price'	, 'relative_height':5, 'function':plot_candlestick },
	# 				'volume'		:{'title':'Volume'	, 'relative_height':1, 'function':plot_volume },
	# 				'macd'			:{'title':'MACD'	, 'relative_height':2, 'function':plot_volume },
	# 				'stochastic'	:{'title':'Stoch'	, 'relative_height':2, 'function':plot_volume },
	# 				}

	# Construct the schemas required for the selected charts
	for chart in scope.charts.keys():
		# print('Checking if we need to render >', chart)
		# print(scope.charts[chart])
		if scope.charts[chart]['active'] == True and scope.charts[chart]['chart_schema'] != None:
			print('Rendering > ', chart)
			no_of_charts += 1
			relative_row_heights.append(scope.charts[chart]['chart_schema']['height'])
			chart_render_list.append(chart)

	# Render the selected Charts
	if no_of_charts > 0:
		row_heights = proportional_row_heights(relative_row_heights)
		
		fig = go.Figure()
		fig = make_subplots(
							rows=no_of_charts, 
							cols=1, 
							shared_xaxes=True,
							vertical_spacing=0.01, 
							row_heights=row_heights		# TODO this does the height of each plot - not sure if this is proportional or otherwise
														# pretty sure it is a percent adding to 100% - so it needs to be somewhat relative - we need a big scale
							)
		
		# plot requested charts
		for chart_no, chart in enumerate(chart_render_list):
			row_no = chart_no+1 
			chart_title = scope.charts[chart]['chart_schema']['title']
			scope.charts[chart]['chart_schema']['function'](fig, chart_title, plot_df, row_no, col_no)

		# add any measures # TODO abstract ths out
		# fig.add_trace(go.Scatter(
		# 					x=plot_df['date'], 
		# 					y=plot_df['sma_1'], 
		# 					opacity=0.7, 
		# 					line=dict(color='blue', width=2), 
		# 					name='sma_1'))





		# format the charts
		fig.update_layout(	
							title=ticker,
							height=scope.chart_height, 
							# width=1200, 
							showlegend=False, 
							xaxis_rangeslider_visible=False,
							margin=go.layout.Margin(l=20, r=20, b=20, t=20)
							# xaxis_rangebreaks=[dict(values=dt_breaks)]
							)
		# Hide Weekends
		fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])
		# output to browser
		st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chart Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def proportional_row_heights(relative_row_heights):
	relative_total = sum(relative_row_heights)

	for pos, relative_height in enumerate(relative_row_heights):
		proportional_height = relative_height / relative_total
		relative_row_heights[pos] = proportional_height

	return relative_row_heights


# =========================================================================================
# Y Axis Format TODO - move into the individual chart rendering!
# =========================================================================================

# Format the Axis
# fig.update_layout(yaxis_tickformat='$',
#               yaxis2_tickformat='$',
#               yaxis3_tickformat='$',
#               yaxis4_tickformat='$',
#               height=750,
#               width=1200,
#               showlegend=False,
#               title_text=Current_Stock_Profile.shortName)
