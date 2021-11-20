import numpy as np



def macd_cols(scope, chart_df, chart):
	# Moving Average, Convergence, Divergence (MACD)

	# MACD = https://www.investopedia.com/terms/m/macd.asp
	
	column 		= scope.charts[chart]['params']['column']
	short 		= scope.charts[chart]['params']['short']
	long 		= scope.charts[chart]['params']['long']
	signal 		= scope.charts[chart]['params']['signal']
		
	chart_df['macd_short'] 		= chart_df[column].ewm(span=short, adjust=False).mean()
	chart_df['macd_long']  		= chart_df[column].ewm(span=long , adjust=False).mean()
	chart_df['macd_col'] 		= chart_df['macd_short'] - chart_df['macd_long']							# black line on ANZ Share Investing
	chart_df['macd_col'] 		= chart_df['macd_col'].ewm(span=signal, adjust=False).mean()			# red line on ANZ Share Investing
	chart_df['macd_histogram'] 	= chart_df['macd_col'] - chart_df['macd_col']						# red & green bar chart on ANZ Share Investing

	# trend direction - when the histogram changes direction - this signals a buy
	chart_df['macd_trend'] 		= np.where( chart_df['macd_histogram'] > chart_df['macd_histogram'].shift(1), 'U', 'D')

	# tag point of crossover
	chart_df['above_or_below']	= np.where( chart_df['macd_col'] > chart_df['macd_col'], 1, 0 )				# Above or Below    1 = MACD is above Signal line. 0 = the MACD is below the signal line
	chart_df['macd_cross'] 		= chart_df['above_or_below'].diff().fillna(0).astype(int)					# Point of Change   1 = cross in up direction and -1 cross down
	chart_df['macd_cross'] 		= np.where( ( chart_df['macd_cross'] == +1), 'x_up',
								  np.where( ( chart_df['macd_cross'] == -1), 'x_dn', 'other' ) )
	
	chart_df['macd_histo_strength'] = np.where( (chart_df['macd_col'] >= -0.5 ) & (chart_df['macd_col'] <= 0.5), 'w', 'S')

	chart_df.drop(['above_or_below'], axis=1, inplace=True)
	


def macd_plot():
	print(macd_plot)




# Copied from the finance tutorial
# macd = MACD(close=share_data['close'], 
# 				window_slow=26,
# 				window_fast=12, 
# 				window_sign=9)


# # Plot MACD trace on 3rd row
# colors = ['green' if val >= 0 else 'red' for val in macd.macd_diff()]
# fig.add_trace(go.Bar(
# 						x=share_data.index, 
# 						y=macd.macd_diff(),
# 						marker_color=colors
# 					), row=3, col=1)										# chart 3 please

# fig.add_trace(go.Scatter(
# 						x=share_data.index,
# 						y=macd.macd(),
# 						line=dict(color='black', width=2)
# 						), row=3, col=1)									# chart 3 please
# fig.add_trace(go.Scatter(
# 						x=share_data.index,
# 						y=macd.macd_signal(),
# 						line=dict(color='blue', width=1)
# 						), row=3, col=1) 									# chart 3 please






def old_plot_macd( params, share_df, fig, axes_candle ):
	axes_macd   = fig.add_axes((0, 0.48, 1, 0.20), sharex = axes_candle )
	
	column_name = determine_original_column_name( params.chart_macd_on_volume['macd'] )

	macd_col_name      = params.chart_macd_on_volume['macd']
	histogram_col_name = params.chart_macd_on_volume['hist']
	signal_col_name    = params.chart_macd_on_volume['sigl']

	# work out colours for the MACD - i.e. below zero = 'red'
	macd_hist_colors = []
   
	for index, row in share_df.iterrows():
		if row[histogram_col_name] > 0: macd_hist_colors.append('green')
		else:                               macd_hist_colors.append('red')
	
	axes_macd.plot (share_df.index, share_df[macd_col_name],          label="macd")
	axes_macd.bar(  share_df.index, share_df[histogram_col_name] * 3, label="hist",   color=macd_hist_colors)
	axes_macd.plot( share_df.index, share_df[signal_col_name],        label="signal")
	axes_macd.set_title('MACD on ' + column_name + ' Column')
	axes_macd.legend()


