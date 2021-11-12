
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


# Library for the Financial Tutorial
import pandas as pd
from ta.trend import MACD
from ta.momentum import StochasticOscillator


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

