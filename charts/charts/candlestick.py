import plotly.graph_objects as go




# candle_cols - No Additional Columns are required to render the CandleStick Chart



def candle_plot(scope, fig, chart, chart_df, row_no, col_no):

	fig.add_trace( 	go.Candlestick(
									x		= chart_df['date'],
									open	= chart_df['open'],
									high	= chart_df['high'],
									low		= chart_df['low'],
									close	= chart_df['close']
								), 
					row=row_no, 
					col=col_no,
					# showlegend=True, This errrors
					)	
	









# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Old Code - TODO - delete this when we are happy with the candlestick
# # -------------------------------------------------------------------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Candlestick Chart - add volume as secondary but linked x axis chart
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# def plot_candlestick_seperate_volume(share_data):

	# show = render_chart_options(2)

	# fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

	# fig.add_trace(go.Candlestick(
	# 							x		= share_data['date'],
	# 							open	= share_data['open'],
	# 							high	= share_data['high'],
	# 							low		= share_data['low'],
	# 							close	= share_data['close'], 
	# 							), row=1, col=1)

	# fig.add_trace(go.Bar(
	# 							x = share_data['date'], 
	# 							y = share_data['volume'],
	# 							marker_color = 'LightSkyBlue', 
	# 							), row=2, col=1)
	
	# # Format the X Axis							
	# fig.update_xaxes(showgrid=False)
	# # if show['weekends'] == 'Hide':
	# # fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])

	# # Format the Y Axis
	# fig.update_yaxes(showgrid=False)
	# fig.update_yaxes(autorange=True) 

	# Add range slider
	# fig.update_layout(
	# 				# title_text="Candlestick",
	# 				height=800,
	# 				yaxis_tickformat='$,.2f',
	# 				updatemenus=[dict(
	# 						type = "buttons",
	# 						direction = "left",
	# 						# https://plotly.com/python/range-slider/
	# 						# https://plotly.com/python/custom-buttons/
	# 						buttons=list([
	# 							dict(
	# 								args=["type", "surface"],
	# 								label="Hide Weekends",
	# 								method="restyle"
	# 								),
	# 							dict(
	# 								args=["type", "heatmap"],
	# 								label="Show Weekends",
	# 								method="restyle"
	# 								)]),
	# 						pad={"r": 10, "t": 10},
	# 						showactive=True,
	# 						x=0.11,
	# 						xanchor="left",
	# 						y=1.1,
	# 						yanchor="top"
	# 					),],
	# 				xaxis=dict(
	# 					rangeselector=dict(
	# 						buttons=list([
	# 							dict(count=1, label="1m",  step="month", stepmode="backward"),
	# 							dict(count=6, label="6m",  step="month", stepmode="backward"),
	# 							dict(count=1, label="YTD", step="year",  stepmode="todate"),
	# 							dict(count=1, label="1y",  step="year",  stepmode="backward"),
	# 							dict(step="all")
	# 						])),
	# 					rangeslider=dict( visible=True ),
	# 					type="date",
	# 					),
					
	# 				yaxis2_tickformat=',.',
					
	# 				showlegend=False,
	# 				)




	# st.plotly_chart(fig, use_container_width=True)



# def plot_candlestick_embedded_volume(share_data):
# 	st.markdown('###### Candlestick Chart < initial 1 >')
# 	# show = render_radio_options(1)
# 	show = render_chart_options(1)
	
# 	layout = go.Layout(yaxis=dict(tickformat=".2%"))

# 	fig = make_subplots(specs=[[{"secondary_y": True}]] )

# 	fig.add_trace(go.Candlestick(
# 								x		= share_data['date'],		# Object
# 								open	= share_data['open'],						# float
# 								high	= share_data['high'],						# float
# 								low		= share_data['low'],							# float
# 								close	= share_data['close'], 						# float
# 								# increasing_line_color= 'cyan', 
# 								# decreasing_line_color= 'gray',
# 								# cscascaca = True, #uncomment this to see all the options
# 								# hoverinfo
# 								# line
# 								# text
# 								# 	Sets hover text elements associated with each sample
# 								# 	point. If a single string, the same string appears over
# 								# 	all the data points. If an array of string, the items
# 								# 	are mapped in order to this trace's sample points.
# 								), secondary_y=True)
	
# 	# include a go.Bar trace for volumes
# 	if show['volume'] == 'Show': fig.add_trace(go.Bar(	
# 													x 			 = share_data['date'], 
# 													y 			 = share_data['volume'],
# 													marker_color = 'LightSkyBlue', # forestgreen steelblue
# 													# yaxis2_tickformat=',.2f',
# 													),
# 													secondary_y=False,
# 											)

# 	# Format the X Axis
# 	fig.update_xaxes(showgrid=False)

# 	if show['weekends'] == 'Hide':
# 		fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])
# 		# fig.update_xaxes(rangebreaks=[{ 'pattern': 'hour', 'bounds':[23,11]}])			# this may come in handy later

# 	# Format the Y Axis
# 	fig.update_yaxes(showgrid=False)
# 	fig.update_yaxes(tickformat=',.') 	
# 	fig.update_yaxes(autorange=True) 
	
# 	fig.update_layout(	
# 						# yaxis_tickformat=',.', 			# this is the volume
#                   		yaxis2_tickformat='$,.2f',			# and this is the candlestick
# 						height=800,
# 						showlegend=False,
# 				  	)

# 	fig.update_layout(xaxis_rangeslider_visible=False)		# Remove the date selection - i dont think we do this
# 	st.plotly_chart(fig, use_container_width=True)



