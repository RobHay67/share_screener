import plotly.graph_objects as go



def stoch_plot(scope, fig, chart, chart_df, row_no, col_no):
	# Stochastic Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['stoch_slow_K'],
								line	= dict(color='blue', width=2),
								), 
					row=row_no, 
					col=col_no,
					)	
	# Signal Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['stoch_slow_D'],
								line	= dict(color='green', width=2),
								), 
					row=row_no, 
					col=col_no,
					)
	# Over Brought Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['stoch_overbuy'],
								line	= dict(color='lightslategray', width=2, dash="dot"),
								), 
					row=row_no, 
					col=col_no,
					)
	# Over Sold Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['stoch_oversold'],
								line	= dict(color='lightslategray', width=2, dash="dot"),
								), 
					row=row_no, 
					col=col_no,
					)

