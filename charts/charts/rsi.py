import numpy as np


def rsi_cols(scope, chart_df, chart):
	# Relative Strength Index (RSI)
	
	# RSI = https://www.investopedia.com/terms/r/rsi.asp

	column 		= scope.charts[chart]['params']['column']
	no_of_days	= scope.charts[chart]['params']['periods']

	chart_df['rsi_delta'] 	= chart_df[column].diff()
	chart_df['rsi_up']		= np.where(chart_df['rsi_delta'] >= 0, chart_df['rsi_delta']     , 0)
	chart_df['rsi_down']  	= np.where(chart_df['rsi_delta'] <  0, chart_df['rsi_delta'] * -1, 0)
	chart_df['rsi_avg_ups'] 		= chart_df['rsi_up'].rolling(window=no_of_days).mean()
	chart_df['rsi_avg_downs'] 	= chart_df['rsi_down'].rolling(window=no_of_days).mean()
	chart_df['rsi_RS']           = chart_df['rsi_avg_ups'] / chart_df['rsi_avg_downs']
	
	chart_df['rsi_trend'] = 100 - ( 100 / ( chart_df['rsi_RS'] + 1 ))
	chart_df['rsi_trend'] = chart_df['rsi_trend'].replace(np.nan, 0)
	chart_df['rsi_trend'] = ( chart_df['rsi_trend'] / 10 ).astype(int)

	# chart_df['rsi_trend'] = np.where( chart_df['rsi_trend'] > 50.0, 'A', 'B' )


def rsi_plot():
	print( ' RSI plot')
