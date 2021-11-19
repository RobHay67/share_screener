import plotly.graph_objects as go




# candle_cols - No Additional Columns are required to render the CandleStick Chart



def candle_plot(fig, chart_title, chart_df, row_no, col_no):
	fig.add_trace( 	go.Candlestick(
									x		= chart_df['date'],
									open	= chart_df['open'],
									high	= chart_df['high'],
									low		= chart_df['low'],
									close	= chart_df['close']
								), 
					row=row_no, 
					col=col_no
					)	
	fig.update_yaxes(title_text=chart_title, row=row_no, col=col_no)














# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Old Code - TODO - delete this when we are happy with the candlestick
# # -------------------------------------------------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# import streamlit as st
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# from analysis.charts.options import render_chart_options


def view_candlestick(share_df):
	print('This is the candlestick')

	fig = basic_candlestick(share_df)
	fig = include_range_slider(fig, False)
	# fig = remove_empty_dates(fig, share_df)
	fig = hide_weekends(fig)




	# fig.show()
	st.plotly_chart(fig, use_container_width=True)

def basic_candlestick(share_df):
	fig = go.Figure(go.Candlestick(
									# x=share_data.index,
									x		= share_df['date'],
									open	= share_df['open'],
									high	= share_df['high'],
									low		= share_df['low'],
									close	= share_df['close'])
					)
	return fig

def include_range_slider(fig, option=True):
	# remove the rangeslider
	fig.update_layout(xaxis_rangeslider_visible=option)
	return fig

def remove_empty_dates(fig, share_df):
	# removing all empty dates
	dt_all = pd.date_range(start=share_df.index[0],end=share_df.index[-1])				# build complete timeline from start date to end date
	dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(share_df.index)]			# retrieve the dates that ARE in the original datset
	dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]	# define dates with missing values
	fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
	return fig

def hide_weekends(fig):
	fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])
	return fig

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Candlestick Chart - add volume as secondary but linked x axis chart
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def plot_candlestick_seperate_volume(share_data):

	show = render_chart_options(2)

	fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

	fig.add_trace(go.Candlestick(
								x		= share_data['date'],
								open	= share_data['open'],
								high	= share_data['high'],
								low		= share_data['low'],
								close	= share_data['close'], 
								), row=1, col=1)

	fig.add_trace(go.Bar(
								x = share_data['date'], 
								y = share_data['volume'],
								marker_color = 'LightSkyBlue', 
								), row=2, col=1)
	
	# Format the X Axis							
	fig.update_xaxes(showgrid=False)
	# if show['weekends'] == 'Hide':
	fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])

	# Format the Y Axis
	fig.update_yaxes(showgrid=False)
	fig.update_yaxes(autorange=True) 

	# Add range slider
	fig.update_layout(
					# title_text="Candlestick",
					height=800,
					yaxis_tickformat='$,.2f',
					updatemenus=[dict(
							type = "buttons",
							direction = "left",
							# https://plotly.com/python/range-slider/
							# https://plotly.com/python/custom-buttons/
							buttons=list([
								dict(
									args=["type", "surface"],
									label="Hide Weekends",
									method="restyle"
									),
								dict(
									args=["type", "heatmap"],
									label="Show Weekends",
									method="restyle"
									)]),
							pad={"r": 10, "t": 10},
							showactive=True,
							x=0.11,
							xanchor="left",
							y=1.1,
							yanchor="top"
						),],
					xaxis=dict(
						rangeselector=dict(
							buttons=list([
								dict(count=1, label="1m",  step="month", stepmode="backward"),
								dict(count=6, label="6m",  step="month", stepmode="backward"),
								dict(count=1, label="YTD", step="year",  stepmode="todate"),
								dict(count=1, label="1y",  step="year",  stepmode="backward"),
								dict(step="all")
							])),
						rangeslider=dict( visible=True ),
						type="date",
						),
					
					yaxis2_tickformat=',.',
					
					showlegend=False,
					)




	st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Candlestick Chart - with Embedded Volume
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def plot_candlestick_embedded_volume(share_data):
	st.markdown('###### Candlestick Chart < initial 1 >')
	# show = render_radio_options(1)
	show = render_chart_options(1)
	
	layout = go.Layout(yaxis=dict(tickformat=".2%"))

	fig = make_subplots(specs=[[{"secondary_y": True}]] )

	fig.add_trace(go.Candlestick(
								x		= share_data['date'],		# Object
								open	= share_data['open'],						# float
								high	= share_data['high'],						# float
								low		= share_data['low'],							# float
								close	= share_data['close'], 						# float
								# increasing_line_color= 'cyan', 
								# decreasing_line_color= 'gray',
								# cscascaca = True, #uncomment this to see all the options
								# hoverinfo
								# line
								# text
								# 	Sets hover text elements associated with each sample
								# 	point. If a single string, the same string appears over
								# 	all the data points. If an array of string, the items
								# 	are mapped in order to this trace's sample points.
								), secondary_y=True)
	
	# include a go.Bar trace for volumes
	if show['volume'] == 'Show': fig.add_trace(go.Bar(	
													x 			 = share_data['date'], 
													y 			 = share_data['volume'],
													marker_color = 'LightSkyBlue', # forestgreen steelblue
													# yaxis2_tickformat=',.2f',
													),
													secondary_y=False,
											)

	# Format the X Axis
	fig.update_xaxes(showgrid=False)

	if show['weekends'] == 'Hide':
		fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])
		# fig.update_xaxes(rangebreaks=[{ 'pattern': 'hour', 'bounds':[23,11]}])			# this may come in handy later

	# Format the Y Axis
	fig.update_yaxes(showgrid=False)
	fig.update_yaxes(tickformat=',.') 	
	fig.update_yaxes(autorange=True) 
	
	fig.update_layout(	
						# yaxis_tickformat=',.', 			# this is the volume
                  		yaxis2_tickformat='$,.2f',			# and this is the candlestick
						height=800,
						showlegend=False,
				  	)

	fig.update_layout(xaxis_rangeslider_visible=False)		# Remove the date selection - i dont think we do this
	st.plotly_chart(fig, use_container_width=True)



