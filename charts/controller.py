import plotly.graph_objects as go
from plotly.subplots import make_subplots


import streamlit as st


from charts.candlestick import view_candlestick

def render_selected_charts(scope, ticker):
	
	# Default Values for start of the run
	no_of_charts = 0
	relative_row_heights = []
	col_no = 1
	chart_render_list = []

	# any measures (SMA or EMA) should have been added at this stage, we just need to know we need to render them
	plot_df = scope.selected[scope.display_page]['analysis_df'][ticker]

	# TODO looks like we add a trace for any overlays to the charts after rendering the chart - where the hell do we store this info
	# TODO height may need to end up be some relative proportion that is then fed into an over all height or number of charts to work out the actual value

	charts_schema = {
					'candlestick'	:{'title':'Price'	, 'relative_height':5, 'function':plot_candlestick },
					'volume'		:{'title':'Volume'	, 'relative_height':1, 'function':plot_volume },
					'macd'			:{'title':'MACD'	, 'relative_height':2, 'function':plot_volume },
					'stochastic'	:{'title':'Stoch'	, 'relative_height':2, 'function':plot_volume },
					}

	# Construct the schemas required for the selected charts
	for chart in charts_schema.keys():
		print('Checking if we need to render >', chart)
		if scope.chart[chart]:
			no_of_charts += 1
			print(charts_schema[chart]['relative_height'])
			relative_row_heights.append(charts_schema[chart]['relative_height'])
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
			chart_title = charts_schema[chart]['title']
			charts_schema[chart]['function'](fig, chart_title, plot_df, row_no, col_no)

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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chart Config
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def plot_candlestick(fig, chart_title, plot_df, row_no, col_no):
	fig.add_trace( 	go.Candlestick(
									x		= plot_df['date'],
									open	= plot_df['open'],
									high	= plot_df['high'],
									low		= plot_df['low'],
									close	= plot_df['close']
								), 
					row=row_no, 
					col=col_no
					)	
	fig.update_yaxes(title_text=chart_title, row=row_no, col=col_no)

def plot_volume(fig, chart_title, plot_df, row_no, col_no):
	# Colour the bars on the chart
	colors = ['green' if row['open'] - row['close'] >= 0 else 'red' for index, row in plot_df.iterrows()]
	
	fig.add_trace(	go.Bar(
							x=plot_df['date'],
							y=plot_df['volume'],
							marker_color=colors
							), 
					row=row_no, 
					col=col_no
					)
	fig.update_yaxes(title_text=chart_title, row=row_no, col=col_no)






# =========================================================================================
# Spare Code
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






	# for key, value in scope.chart.items():
	# 	print( key.ljust(20), value)


# print ( '='*80)

# if scope.chart['candlestick']:
# 	no_of_charts += 1
# 	print ('render the candlestick')
# 	# view_candlestick(analysis_df)

# if scope.chart['volume']:
# 	print ('render the volume bar chart')


# if scope.chart['line']:
# 	print ('render the line')

# if scope.chart['macd']:
# 	print ('render the macd')

# if scope.chart['stochastic']:
# 	print ('render the stochastic')

# if scope.chart['ichi_moku']:
# 	print ('render the ichi_moku')

# if scope.chart['heiken_ashi']:
# 	print ('render the heiken_ashi')

# if scope.chart['vac']:
# 	print ('render the vac')

# if scope.chart['vol_osclillator']:
# 	print ('render the vol_osclillator')

# if scope.chart['bollinger_bands']:
# 	print ('render the bollinger_bands')

# if scope.chart['dividends']:
# 	print ('render the dividends')

# if scope.chart['announcements']:
# 	print ('render the announcements')
