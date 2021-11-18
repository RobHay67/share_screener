import numpy as np


def rsi(scope, plot_df, chart):
	# Relative Strength Index (RSI)
	
	# RSI = https://www.investopedia.com/terms/r/rsi.asp

	column 		= scope.charts[chart]['params']['column']
	no_of_days	= scope.charts[chart]['params']['periods']

	plot_df['rsi_delta'] 	= plot_df[column].diff()
	plot_df['rsi_up']		= np.where(plot_df['rsi_delta'] >= 0, plot_df['rsi_delta']     , 0)
	plot_df['rsi_down']  	= np.where(plot_df['rsi_delta'] <  0, plot_df['rsi_delta'] * -1, 0)
	plot_df['rsi_avg_ups'] 		= plot_df['rsi_up'].rolling(window=no_of_days).mean()
	plot_df['rsi_avg_downs'] 	= plot_df['rsi_down'].rolling(window=no_of_days).mean()
	plot_df['rsi_RS']           = plot_df['rsi_avg_ups'] / plot_df['rsi_avg_downs']
	
	plot_df['rsi_trend'] = 100 - ( 100 / ( plot_df['rsi_RS'] + 1 ))
	plot_df['rsi_trend'] = plot_df['rsi_trend'].replace(np.nan, 0)
	plot_df['rsi_trend'] = ( plot_df['rsi_trend'] / 10 ).astype(int)

	# plot_df['rsi_trend'] = np.where( plot_df['rsi_trend'] > 50.0, 'A', 'B' )



