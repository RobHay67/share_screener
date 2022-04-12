import numpy as np



def macd_cols(scope, chart_df, chart):
	# Moving Average, Convergence, Divergence (MACD)

	# MACD = https://www.investopedia.com/terms/m/macd.asp
	
	column 	= scope.config['charts'][chart]['add_columns']['column']
	short 	= scope.config['charts'][chart]['add_columns']['short']
	long 	= scope.config['charts'][chart]['add_columns']['long']
	signal 	= scope.config['charts'][chart]['add_columns']['signal']
		
	chart_df['macd_short'] 		= chart_df[column].ewm(span=short, adjust=False).mean()
	chart_df['macd_long']  		= chart_df[column].ewm(span=long , adjust=False).mean()
	chart_df['macd_col'] 		= chart_df['macd_short'] - chart_df['macd_long']							# black line on ANZ Share Investing					# MACD_dff?
	chart_df['macd_signal'] 	= chart_df['macd_col'].ewm(span=signal, adjust=False).mean()				# red line on ANZ Share Investing
	chart_df['macd_histogram'] 	= chart_df['macd_col'] - chart_df['macd_signal']							# red & green bar chart on ANZ Share Investing

	# trend direction - when the histogram changes direction - this signals a buy
	chart_df['macd_trend'] 		= np.where( chart_df['macd_histogram'] > chart_df['macd_histogram'].shift(1), 'U', 'D')

	# tag point of crossover
	chart_df['above_or_below']	= np.where( chart_df['macd_col'] > chart_df['macd_signal'], 1, 0 )			# Above or Below    1 = MACD is above Signal line. 0 = the MACD is below the signal line
	chart_df['macd_cross'] 		= chart_df['above_or_below'].diff().fillna(0).astype(int)					# Point of Change   1 = cross in up direction and -1 cross down
	chart_df['macd_cross'] 		= np.where( ( chart_df['macd_cross'] == +1), 'x_up',
								  np.where( ( chart_df['macd_cross'] == -1), 'x_dn', 'other' ) )
	
	chart_df['macd_histo_strength'] = np.where( (chart_df['macd_col'] >= -0.5 ) & (chart_df['macd_col'] <= 0.5), 'w', 'S')

	chart_df.drop(['above_or_below'], axis=1, inplace=True)