import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# import matplotlib.pyplot as plt
# from matplotlib.pylab import date2num
# from mplfinance.original_flavor import candlestick_ohlc
# import mplfinance as mpf


# TODO - Rob - just work on the end of day data and when we get this working we can wire in the 5 minute data





# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Render Candlestick Chart
# -------------------------------------------------------------------------------------------------------------------------------------------------------------


def plot_candlestick(share_data):
	# st.title('Chart of all available ' + ticker + ' data < candle stick format >') 
	# Options
	show_weekends = st.radio( 	"weekends", ('Hide','Show') )
	show_volume = st.radio( 	"volume", ('Hide','Show') )

	print('show_weekends = ', show_weekends)

	layout = go.Layout(yaxis=dict(tickformat=".2%"))

	fig = make_subplots(specs=[[{"secondary_y": True}]] )

	fig.add_trace(go.Candlestick(
	# fig = go.Figure( data=[go.Candlestick(
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
								# )])
	
	# include a go.Bar trace for volumes
	if show_volume == 'Show':
		fig.add_trace(go.Bar(	x 			 = share_data['date'], 
								y 			 = share_data['volume'],
								marker_color = 'LightSkyBlue', # forestgreen steelblue
							),
							secondary_y=False,
						)

	if show_weekends == 'Hide':
		fig.update_xaxes(
			rangebreaks=[
						{ 'pattern': 'day of week', 'bounds': [6, 1]}
						# { 'pattern': 'hour', 'bounds':[23,11]}
						]
						)
	
	# Format the Figure
	fig.layout.xaxis.showgrid=False
	fig.update_layout(	yaxis_tickformat=',.', # this is the volume
                  		yaxis2_tickformat=',.2f',	# and this is the candlestick
						  height=800,
						  showlegend=False,
				  	)


	# Turn off the grid??
	# fig.layout.yaxis2.showgrid=False
	
	# fig.layout.yaxis.showgrid=False
	# fig.layout.xaxis2.showgrid=False

	# fig['layout']['yaxis'].update(autorange = True)

	print(fig)
	# fig.show()
	# fig.update_layout(xaxis_rangeslider_visible=False)		# Remove the date selection - i dont think we do this
	st.plotly_chart(fig, use_container_width=True)


def plot_basic_chart(scope, ticker):
	st.write('Chart of all available ' + ticker + ' data') 

	if ticker in list(scope.share_data_files.keys()):
		share_data = scope.share_data_files[ticker]
		fig = go.Figure(
				data=go.Scatter(x=share_data['date'], y=share_data['close'])
			)
		# print ( '='*100)
		# print('fig from plot basic chart ') 
		# print(fig)
		# print ( '='*100)
		fig.update_layout(
			title={
				'text': "Stock Prices Over Past ??????? Years",
				'y':0.9,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'})
		st.plotly_chart(fig, use_container_width=True)
	else:
		st.error('Load / Download some ticker data')

		# start = dt.datetime.today()-dt.timedelta(2 * 365)
		# end = dt.datetime.today()
		# df = yf.download(ticker,start,end)
		# df = df.reset_index()
		# fig = go.Figure(
		# 		data=go.Scatter(x=df['Date'], y=df['Adj Close'])
		# 	)


def plot_chart( params, share_df, ticker ):
	# chart_df   = share_df.copy()
	# %matplotlib tk
	share_df = share_df.iloc[-params.analysis_no_of_days:]                        # Filter number of observations for plot
	
	# Create figure, set axes and plot the candlestick graph (always)
	fig = plt.figure()
	fig.set_size_inches((20, 10))   							# w / h
	# plt.style.use('dark_background')
	axes_candle = fig.add_axes((0, 0.72, 1, 0.32))              # The dimensions [left, bottom, width, height] of the new axes.
	axes_candle.xaxis_date()                                    # Format x-axis ticks as dates
	
	plot_candlestick( params, share_df, axes_candle, ticker )                       
   
	# Save the chart as PNG
#     fig.savefig("charts/" + ticker + ".png", bbox_inches="tight")
	
	plt.show()



def test_plots(scope, ticker):
	df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

	# print(df)
	# print(df.dtypes)

	fig = go.Figure(data=[go.Candlestick(x=df['Date'],		# Object
                open=df['AAPL.Open'],						# float
                high=df['AAPL.High'],						# float
                low=df['AAPL.Low'],							# float
                close=df['AAPL.Close'])])					# float

	# fig.show()
	st.plotly_chart(fig, use_container_width=True)



def plot_candlestick_original( params, share_data, axes_candle, ticker ): 
	# Get nested list of date, open, high, low and close prices
	ohlc = []

	for date, row in share_data.iterrows():
		openp, highp, lowp, closep = row[:4]
		ohlc.append([date2num(date), openp, highp, lowp, closep])

	axes_candle.set_title( ticker.upper() + ' - ' + params.share_index.at[ticker, 'company_name'] )
	
	for chart_line in params.chart_lines: 
		axes_candle.plot( share_data.index, share_data[chart_line], label=chart_line )

    # ax_candle.scatter( share_df.index, share_df['trade_buy' ],   label = 'Buy',  marker = 'X', color = 'blue' )
    # ax_candle.scatter( share_df.index, share_df['trade_sell'],   label = 'Sell', marker = 'v', color = 'orange'   )
	
	candlestick_ohlc( axes_candle, ohlc, colorup='g', colordown='r', width=0.3 )
	axes_candle.legend()











# Redundant Code below - keep for the moment



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