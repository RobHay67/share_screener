import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Library for the Financial Tutorial
import pandas as pd
from ta.trend import MACD
from ta.momentum import StochasticOscillator

# TODO - Rob - just work on the end of day data and when we get this working we can wire in the 5 minute data




def financial_chart_tutorial(share_data):
	# https://python.plainenglish.io/a-simple-guide-to-plotly-for-plotting-financial-chart-54986c996682

	print('test')

	fig = go.Figure(go.Candlestick(x=share_data.index,
		open=share_data['open'],
		high=share_data['high'],
		low=share_data['low'],
		close=share_data['close']))

	# removing rangeslider
	fig.update_layout(xaxis_rangeslider_visible=False)

	
	# hide weekends
	# fig.update_xaxes(rangebreaks=[dict(bounds=["sat", "mon"])])

	# removing all empty dates
	# build complete timeline from start date to end date
	dt_all = pd.date_range(start=share_data.index[0],end=share_data.index[-1])
	# retrieve the dates that ARE in the original datset
	dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(share_data.index)]
	# define dates with missing values
	dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]
	fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])


	# TODO Rob note that the dataframe may need to be sorted in ascending order for these to work correctly - probably best to apply these 
	# measures before doing the sort - or maybe change the data displayers to sort and then un-sort

	# add moving averages to dataframe
	share_data.sort_values(by=['date'], inplace=True, ascending=True)	
	share_data['MA20'] = share_data['close'].rolling(window=20).mean()
	share_data['MA5'] = share_data['close'].rolling(window=5).mean()

	fig.add_trace(go.Scatter(x=share_data.index, 
                         y=share_data['MA5'], 
                         opacity=0.7, 
                         line=dict(color='blue', width=2), 
                         name='MA 5'))
	fig.add_trace(go.Scatter(x=share_data.index, 
                         y=share_data['MA20'], 
                         opacity=0.7, 
                         line=dict(color='orange', width=2), 
                         name='MA 20'))


	# first declare an empty figure
	fig = go.Figure()
	# add OHLC trace
	# fig.add_trace(go.Candlestick(x=share_data.index,
	# 							open=share_data['open'],
	# 							high=share_data['high'],
	# 							low=share_data['low'],
	# 							close=share_data['close'], 
	# 							showlegend=False))
	# # add moving average traces
	# fig.add_trace(go.Scatter(x=share_data.index, 
	# 						y=share_data['MA5'], 
	# 						opacity=0.7, 
	# 						line=dict(color='blue', width=2), 
	# 						name='MA 5'))
	# fig.add_trace(go.Scatter(x=share_data.index, 
	# 						y=share_data['MA20'], 
	# 						opacity=0.7, 
	# 						line=dict(color='orange', width=2), 
	# 						name='MA 20'))
	# # hide dates with no values
	# fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
	# # remove rangeslider
	# fig.update_layout(xaxis_rangeslider_visible=False)
	# # add chart title 
	# fig.update_layout(title="AAPL")

	



	# MACD
	macd = MACD(close=share_data['close'], 
				window_slow=26,
				window_fast=12, 
				window_sign=9)
	# stochastic
	stoch = StochasticOscillator(high=share_data['high'],
								close=share_data['close'],
								low=share_data['low'],
								window=14, 
								smooth_window=3)

	# fig = make_subplots(rows=4, cols=1, shared_xaxes=True)
	# add subplot properties when initializing fig variable
	fig = make_subplots(rows=4, cols=1, shared_xaxes=True,
                    vertical_spacing=0.01, 
                    row_heights=[0.5,0.1,0.2,0.2])				# this does the heigh of each plot - not sure if this is proportional or otherwise

	# update y-axis label										# this add the labels to each plot along the side
	fig.update_yaxes(title_text="Price", row=1, col=1)
	fig.update_yaxes(title_text="Volume", row=2, col=1)
	fig.update_yaxes(title_text="MACD", showgrid=False, row=3, col=1)
	fig.update_yaxes(title_text="Stoch", row=4, col=1)

	#TODO - Rob I copied the code from above

	# Plot OHLC on 1st subplot (using the codes from before)

	fig.add_trace(go.Candlestick(x=share_data.index,	
								open=share_data['open'],
								high=share_data['high'],
								low=share_data['low'],
								close=share_data['close'], 
								showlegend=False))
	
	# add moving average traces
	fig.add_trace(go.Scatter(x=share_data.index, 
							y=share_data['MA5'], 
							opacity=0.7, 
							line=dict(color='blue', width=2), 
							name='MA 5'))
	
	fig.add_trace(go.Scatter(x=share_data.index, 
							y=share_data['MA20'], 
							opacity=0.7, 
							line=dict(color='orange', width=2), 
							name='MA 20'))
	
	
	
	
	# hide dates with no values
	fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
	# remove rangeslider
	fig.update_layout(xaxis_rangeslider_visible=False)
	# add chart title 
	fig.update_layout(title="AAPL")





	# Plot volume trace on 2nd row 
	# fig.add_trace(go.Bar(x=share_data.index, 
	# 					y=share_data['volume']
	# 					), row=2, col=1)

	# Plot volume trace on 2nd row - TODO Alternative -
	colors = ['green' if row['open'] - row['close'] >= 0 
          else 'red' for index, row in share_data.iterrows()]
	fig.add_trace(go.Bar(x=share_data.index, 
                     y=share_data['volume'],
                     marker_color=colors
                    ), row=2, col=1)




	# Plot MACD trace on 3rd row
	# fig.add_trace(go.Bar(x=share_data.index, 
	# 					y=macd.macd_diff()
	# 					), row=3, col=1)
	colors = ['green' if val >= 0 
			else 'red' for val in macd.macd_diff()]
	fig.add_trace(go.Bar(x=share_data.index, 
                     y=macd.macd_diff(),
                     marker_color=colors
                    ), row=3, col=1)

	fig.add_trace(go.Scatter(x=share_data.index,
							y=macd.macd(),
							line=dict(color='black', width=2)
							), row=3, col=1)
	fig.add_trace(go.Scatter(x=share_data.index,
							y=macd.macd_signal(),
							line=dict(color='blue', width=1)
							), row=3, col=1)


	# Plot MACD trace on 3rd row - TODO - Alternative
	



	# Plot stochastics trace on 4th row
	fig.add_trace(go.Scatter(x=share_data.index,
							y=stoch.stoch(),
							line=dict(color='black', width=2)
							), row=4, col=1)
	fig.add_trace(go.Scatter(x=share_data.index,
							y=stoch.stoch_signal(),
							line=dict(color='blue', width=1)
							), row=4, col=1)
	# update layout by changing the plot size, hiding legends & rangeslider, and removing gaps between dates
	fig.update_layout(height=900, width=1200, 
					showlegend=False, 
					xaxis_rangeslider_visible=False,
					xaxis_rangebreaks=[dict(values=dt_breaks)])

	# removing white space									# TODO - expalnds the plots into the whitespace - cool
	fig.update_layout(margin=go.layout.Margin(
								l=20, #left margin
								r=20, #right margin
								b=20, #bottom margin
								t=20  #top margin
							))

	print(share_data.columns)
	fig.show()
	# st.plotly_chart(fig, use_container_width=True)


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


def plot_candlestick(share_data):
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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Line Chart
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def plot_line_chart(share_data):
	st.markdown('##### Line Chart')

	# show = render_radio_options(33)
	show = render_chart_options(33, show_col_checkboxes=True)

	if show['volume'] == 'Show': show['columns']['volume'] = 'LightSkyBlue'

	fig = make_subplots(specs=[[{"secondary_y": True}]])

	x_data = share_data['date']
	for col_name, col_colour in show['columns'].items():
		if col_name != 'volume'	: plot_type, secondary = go.Scatter	, True
		else					: plot_type, secondary = go.Bar		, False

		fig.add_trace(plot_type(
									x = x_data,
									y 		= share_data[col_name],
									name	= col_name,
									marker_color = col_colour,
								), secondary_y=secondary)
	
	if show['weekends'] == 'Hide':
		fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])

	fig.update_layout(height=800)

	st.plotly_chart(fig, use_container_width=True)






# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Charting Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_chart_options(unique_key, show_col_checkboxes=False):

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

	with col1: st.write('Select Options')
	# Options for the chart
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: left;}</style>', unsafe_allow_html=True)
	with col2: show_weekends 	= st.radio("weekends", ('Hide','Show'), key=unique_key)
	with col3: show_volume 		= st.radio("volume"  , ('Hide','Show'), key=unique_key)

	# build the list of columns
	columns_to_plot = {}
	if show_col_checkboxes:
		with col4: open = st.checkbox('open', key=unique_key)
		with col5: high = st.checkbox('high', key=unique_key)
		with col6: low = st.checkbox('low', key=unique_key)
		with col7: close = st.checkbox('close', key=unique_key, value=True)
		# with col5: vol = st.checkbox('volume', key=unique_key)

		if open: columns_to_plot['open'] = 'blue'
		if high: columns_to_plot['high'] = 'green'
		if low: columns_to_plot['low'] = 'red'
		if close: columns_to_plot['close'] = 'black'
		# if vol: columns_to_plot['volume'] = 'LightSkyBlue'

	return {'weekends':show_weekends, 'volume':show_volume, 'columns':columns_to_plot }




# -------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Chart
# -------------------------------------------------------------------------------------------------------------------------------------------------------------






# ==============================================================================================================================================================
#
# Redundant Code below - keep for the moment
#
# ==============================================================================================================================================================


# def plot_candlestick_original( params, share_data, axes_candle, ticker ): 
# 	# Get nested list of date, open, high, low and close prices
# 	ohlc = []

# 	for date, row in share_data.iterrows():
# 		openp, highp, lowp, closep = row[:4]
# 		ohlc.append([date2num(date), openp, highp, lowp, closep])

# 	axes_candle.set_title( ticker.upper() + ' - ' + params.share_index.at[ticker, 'company_name'] )
	
# 	for chart_line in params.chart_lines: 
# 		axes_candle.plot( share_data.index, share_data[chart_line], label=chart_line )

#     # ax_candle.scatter( share_df.index, share_df['trade_buy' ],   label = 'Buy',  marker = 'X', color = 'blue' )
#     # ax_candle.scatter( share_df.index, share_df['trade_sell'],   label = 'Sell', marker = 'v', color = 'orange'   )
	
# 	candlestick_ohlc( axes_candle, ohlc, colorup='g', colordown='r', width=0.3 )
# 	axes_candle.legend()

# from plotly.subplots import make_subplots
# import plotly.express as px

# import matplotlib.pyplot as plt
# from matplotlib.pylab import date2num
# from mplfinance.original_flavor import candlestick_ohlc
# import mplfinance as mpf




# def plot_line_chart(share_data):

# 	columns_to_plot = render_checkbox_options()

# 	if 'volume' in columns_to_plot: 
# 		st.info('Change Scale if User selects VOLUME')

# 	fig = px.line(share_data, x="date", y=columns_to_plot ) 
	
# 	fig.update_xaxes(showgrid=False)
# 	fig.update_yaxes(tickformat='$,.2f')

# 	st.plotly_chart(fig, use_container_width=True)




# def select_column():
# 	available_ticker_columns = ['open', 'high', 'low', 'close', 'volume']
# 	index_for_close_column = available_ticker_columns.index('close')

# 	col1,col2 = st.columns([2,2])
# 	with col1: selected_ticker_column = st.selectbox( 	'column(s)', 
# 														available_ticker_columns, 
# 														index=index_for_close_column, 
# 														help='choose a ticker column to plot', 
# 														key='21' )

# 	st.write('<style>div.row-widget.stCheckbox > div{flex-direction:row;justify-content: left;}</style>', unsafe_allow_html=True)

	# return selected_ticker_column


# def plot_line_chart_original(share_data):
	
# 	columns_to_plot = render_checkbox_options(1)

# 	fig = go.Figure()

# 	for col_name, col_colour in columns_to_plot.items():

# 		print('Plotting ', col_name, ' with colour of ', col_colour)
# 		plot_line = go.Scatter(
# 								x 		= share_data['date'], 
# 								y 		= share_data[col_name],
# 								# mode 	= 'lines',
# 								name	= col_name,
# 								marker_color = col_colour,
# 								# line 	= dict(color=col_colour)
# 							)
# 		fig.add_trace(plot_line)
	
# 	fig.update_layout(height=800)

# 	st.plotly_chart(fig, use_container_width=True)


# def test_plots(scope, ticker):
# 	share_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# 	# print(share_data)
# 	# print(share_data.dtypes)

# 	fig = go.Figure(data=[go.Candlestick(x=share_data['Date'],		# Object
#                 open=share_data['AAPL.Open'],						# float
#                 high=share_data['AAPL.High'],						# float
#                 low=share_data['AAPL.Low'],							# float
#                 close=share_data['AAPL.Close'])])					# float

# 	# fig.show()
# 	st.plotly_chart(fig, use_container_width=True)


# def plot_chart( params, share_df, ticker ):
# 	# chart_df   = share_df.copy()
# 	# %matplotlib tk
# 	share_df = share_df.iloc[-params.analysis_no_of_days:]                        # Filter number of observations for plot
	
# 	# Create figure, set axes and plot the candlestick graph (always)
# 	fig = plt.figure()
# 	fig.set_size_inches((20, 10))   							# w / h
# 	# plt.style.use('dark_background')
# 	axes_candle = fig.add_axes((0, 0.72, 1, 0.32))              # The dimensions [left, bottom, width, height] of the new axes.
# 	axes_candle.xaxis_date()                                    # Format x-axis ticks as dates
	
# 	plot_candlestick( params, share_df, axes_candle, ticker )                       
   
# 	# Save the chart as PNG
# #     fig.savefig("charts/" + ticker + ".png", bbox_inches="tight")
	
# 	plt.show()


# def plot_basic_chart(scope, ticker):
# 	# st.write('Chart of all available ' + ticker + ' data') 

# 	if ticker in list(scope.share_data_files.keys()):
# 		share_data = scope.share_data_files[ticker]
# 		fig = go.Figure(
# 				data=go.Scatter(x=share_data['date'], y=share_data['close'])
# 			)
# 		# print ( '='*100)
# 		# print('fig from plot basic chart ') 
# 		# print(fig)
# 		# print ( '='*100)
# 		fig.update_layout(
# 			title={
# 				'text': "Stock Prices Over Past ??????? Years",
# 				'y':0.9,
# 				'x':0.5,
# 				'xanchor': 'center',
# 				'yanchor': 'top'})
# 		st.plotly_chart(fig, use_container_width=True)
# 	else:
# 		st.error('Load / Download some ticker data')

# 		# start = dt.datetime.today()-dt.timedelta(2 * 365)
# 		# end = dt.datetime.today()
# 		# share_data = yf.download(ticker,start,end)
# 		# share_data = share_data.reset_index()
# 		# fig = go.Figure(
# 		# 		data=go.Scatter(x=share_data['Date'], y=share_data['Adj Close'])
# 		# 	)



# def plot_candlestick(scope, ticker):
# 	st.title('Chart of all available ' + ticker + ' data < candle stick format >') 
# 	if ticker in list(scope.share_data_files.keys()):
# 		plot_data = scope.share_data_files[ticker].copy()

# 		plot_data.set_index('date', inplace=True)

# 		# print(plot_data)
# 		# print(plot_data.dtypes)

# 		# fig = mpf.Figure(
# 		# 		data=go.Scatter(x=share_data['date'], y=share_data['close'])
# 		# 	)

# 		# Lets try https://github.com/matplotlib/mplfinance/blob/master/examples/external_axes.ipynb
# 		fig = mpf.figure(style='yahoo',figsize=(7,8))
# 		ax1 = fig.add_subplot(2,1,1)
# 		ax2 = fig.add_subplot(2,1,2)

# 		mpf.plot(plot_data,ax=ax1,volume=ax2)

# 		print ( '='*100)
# 		print('fig from plot CANDLESTICK') 
# 		print(fig)
# 		print ( '='*100)


# 		mpf.plot(plot_data,ax=ax1,volume=ax2, savefig='test-fig.png')


# 		# mpf.plot(plot_data,volume=True,tight_layout=True,figscale=0.75)
# 		st.plotly_chart(fig, use_container_width=True)



# 		# ok - this works but only dumps to a PNG
# 		# Plot candlestick.
# 		# Add volume.
# 		# Add moving averages: 3,6,9.
# 		# Save graph to *.png.
# 		mpf.plot(plot_data, type='candle', style='charles',   # tight option??
# 					title='S&P 500, Nov 2019',
# 					ylabel='Price ($)',
# 					ylabel_lower='Shares \nTraded',
# 					volume=True, 
# 					mav=(3,6,9), 
# 					savefig='test-mplfiance.png',
# 					)

# 		# st.plotly_chart(fig, use_container_width=True)


# 		# st.info('Plot the Candlestick right here RObbie')

# 		# fig = plt.figure()

# 		# axes_candle = fig.add_axes((0, 0.72, 1, 0.32))              # The dimensions [left, bottom, width, height] of the new axes.
# 		# axes_candle.xaxis_date()                                    # Format x-axis ticks as dates

# 		# ohlc = []

# 		# for date, row in share_data.iterrows():
# 		# 	openp, highp, lowp, closep = row[:4]
# 		# 	ohlc.append([date2num(date), openp, highp, lowp, closep])

# 		# print (ohlc)
# 		# # axes_candle.set_title( ticker.upper() + ' - ' + params.share_index.at[ticker, 'company_name'] )
	
# 		# # for chart_line in scope.chart_lines: 
# 		# # 	axes_candle.plot( share_data.index, share_data[chart_line], label=chart_line )


# 		# candlestick_ohlc( axes_candle, ohlc, colorup='g', colordown='r', width=0.3 )


# this is the initial caller
# plot_chart( params, analysis_df, ticker )




# def render_radio_options(unique_key):
# 	col1,col2 = st.columns([2,2])

# 	# Options for the chart
# 	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: left;}</style>', unsafe_allow_html=True)
# 	with col1: show_weekends 	= st.radio("weekends", ('Hide','Show'), key=unique_key)
# 	with col2: show_volume 		= st.radio("volume"  , ('Hide','Show'), key=unique_key)

# 	return {'weekends':show_weekends, 'volume':show_volume}

# def render_checkbox_options(unique_key):
# 	col1,col2,col3,col4,col5 = st.columns(5)
# 	with col1: option_1 = st.checkbox('open', key=unique_key)
# 	with col2: option_2 = st.checkbox('high', key=unique_key)
# 	with col3: option_3 = st.checkbox('low', key=unique_key)
# 	with col4: option_4 = st.checkbox('close', key=unique_key, value=True)
# 	with col5: option_5 = st.checkbox('volume', key=unique_key)

# 	# build the list of columns
# 	columns_to_plot = {}

# 	if option_1: columns_to_plot['open'] = 'blue'
# 	if option_2: columns_to_plot['high'] = 'green'
# 	if option_3: columns_to_plot['low'] = 'red'
# 	if option_4: columns_to_plot['close'] = 'black'
# 	if option_5: columns_to_plot['volume'] = 'LightSkyBlue'

# 	return columns_to_plot