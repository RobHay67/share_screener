
import plotly.graph_objects as go



def sma_cols(scope, chart_df, chart):
	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	column 		= scope.charts[chart]['data_cols']['column']
	no_of_days 	= scope.charts[chart]['data_cols']['periods']

	chart_df[chart] = chart_df[column].rolling(window=no_of_days).mean()




def sma_plot(fig, overlay, chart_df, row_no, col_no):
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




