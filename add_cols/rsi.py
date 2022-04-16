

import numpy as np



def rsi_cols(scope, chart_df, chart):
	# Relative Strength Index (RSI)
	
	# RSI = https://www.investopedia.com/terms/r/rsi.asp

	# https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/   Python Calculation methodology

	column 			= scope.config['charts'][chart]['add_columns']['column']
	lookback_days	= scope.config['charts'][chart]['add_columns']['lookback_days']

	chart_df['rsi_delta'] 		= chart_df[column].diff()
	chart_df['rsi_gain']		= np.where(chart_df['rsi_delta'] >= 0, chart_df['rsi_delta']     , 0)
	chart_df['rsi_loss']  		= np.where(chart_df['rsi_delta'] <  0, chart_df['rsi_delta'] * -1, 0)
	chart_df['rsi_avg_gains'] 	= chart_df['rsi_gain'].rolling(window=lookback_days).mean()
	chart_df['rsi_avg_losses'] 	= chart_df['rsi_loss'].rolling(window=lookback_days).mean()
	chart_df['rsi_rs']          = chart_df['rsi_avg_gains'] / chart_df['rsi_avg_losses']
	chart_df['rsi']          	= 100 - ( 100 / ( chart_df['rsi_rs'] +1 ))

	chart_df['rsi'] = chart_df['rsi'] / 100

	chart_df['rsi_overbuy'] 	= 0.7
	chart_df['rsi_oversold'] 	= 0.3

	chart_df['rsi_trend'] = 100 - ( 100 / ( chart_df['rsi_rs'] + 1 ))
	chart_df['rsi_trend'] = chart_df['rsi_trend'].replace(np.nan, 0)
	chart_df['rsi_trend'] = ( chart_df['rsi_trend'] / 10 ).astype(int)