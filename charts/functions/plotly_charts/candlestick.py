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
	




