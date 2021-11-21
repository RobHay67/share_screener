import numpy as np
import plotly.graph_objects as go


def rsi_cols(scope, chart_df, chart):
	# Relative Strength Index (RSI)
	
	# RSI = https://www.investopedia.com/terms/r/rsi.asp

	# https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/   Python Calculation methodology

	column 			= scope.charts[chart]['data_cols']['column']
	lookback_days	= scope.charts[chart]['data_cols']['lookback_days']

	chart_df['rsi_delta'] 		= chart_df[column].diff()
	chart_df['rsi_gain']		= np.where(chart_df['rsi_delta'] >= 0, chart_df['rsi_delta']     , 0)
	chart_df['rsi_loss']  		= np.where(chart_df['rsi_delta'] <  0, chart_df['rsi_delta'] * -1, 0)
	chart_df['rsi_avg_gains'] 	= chart_df['rsi_gain'].rolling(window=lookback_days).mean()
	chart_df['rsi_avg_losses'] 	= chart_df['rsi_loss'].rolling(window=lookback_days).mean()
	chart_df['rsi_rs']          = chart_df['rsi_avg_gains'] / chart_df['rsi_avg_losses']
	chart_df['rsi']          	= 100 - ( 100 / ( chart_df['rsi_rs'] +1 ))
	# print ( chart_df)

	chart_df['rsi'] = chart_df['rsi'] / 100

	chart_df['rsi_overbuy'] 	= 0.7
	chart_df['rsi_oversold'] 	= 0.3

	chart_df['rsi_trend'] = 100 - ( 100 / ( chart_df['rsi_rs'] + 1 ))
	chart_df['rsi_trend'] = chart_df['rsi_trend'].replace(np.nan, 0)
	chart_df['rsi_trend'] = ( chart_df['rsi_trend'] / 10 ).astype(int)


	# share_df['rsi']          = 100 - ( 100 / ( share_df['RS'] +1 ))
	# chart_df['rsi_trend'] = np.where( chart_df['rsi_trend'] > 50.0, 'A', 'B' )


def rsi_plot(scope, fig, chart, chart_df, row_no, col_no):
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['rsi'],
								line	= dict(color='blue', width=2),
								), 
					row=row_no, 
					col=col_no,
					)	

		# Over Brought Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['rsi_overbuy'],
								line	= dict(color='lightslategray', width=2, dash="dot"),
								), 
					row=row_no, 
					col=col_no,
					)
	# Over Sold Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['rsi_oversold'],
								line	= dict(color='lightslategray', width=2, dash="dot"),
								), 
					row=row_no, 
					col=col_no,
					)




