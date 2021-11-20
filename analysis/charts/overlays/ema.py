import plotly.graph_objects as go


def ema_cols( scope, chart_df, chart):
	# add an Exponential Moving Average (EMA)
	
	# EMA  = https://www.investopedia.com/terms/e/ema.asp

	column 		= scope.charts[chart]['data_cols']['column']
	no_of_days 	= scope.charts[chart]['data_cols']['periods']

	chart_df[chart] = chart_df[column].ewm(span=no_of_days, adjust=False).mean()



def ema_plot(fig, overlay, chart_df, row_no, col_no):
	fig.add_trace(go.Scatter(
								x		= chart_df['date'], 
								y		= chart_df[overlay], 
								opacity	= 0.7, 
								line	= dict(color='blue', width=2), 
								name	= overlay
							), 
					row		= row_no, 
					col		= col_no
				)