import plotly.graph_objects as go
	
def macd_plot(scope, fig, chart, chart_df, row_no, col_no):

	histogram_colours = ['seagreen' if row['macd_histogram'] >=0 else 'salmon' for index, row in chart_df.iterrows()]

	# MACD (diff) Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['macd_col'],
								line	= dict(color='blue', width=2),
								), 
					row=row_no, 
					col=col_no,
					)									

	# Signal Line
	fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df['macd_signal'],
								line	= dict(color='red', width=1),
								), 
					row=row_no, 
					col=col_no,
					)

	# Histogram Columns
	fig.add_trace(	go.Bar(
							x		= chart_df['date'],
							y		= chart_df['macd_histogram'],
							marker_color	= histogram_colours,
							), 
					row=row_no, 
					col=col_no,
					)











# def old_plot_macd( params, share_df, fig, axes_candle ):
# 	axes_macd   = fig.add_axes((0, 0.48, 1, 0.20), sharex = axes_candle )
	
# 	column_name = determine_original_column_name( params.chart_macd_on_volume['macd'] )

# 	macd_col_name      = params.chart_macd_on_volume['macd']
# 	histogram_col_name = params.chart_macd_on_volume['hist']
# 	signal_col_name    = params.chart_macd_on_volume['sigl']

# 	# work out colours for the MACD - i.e. below zero = 'red'
# 	macd_hist_colors = []
   
# 	for index, row in share_df.iterrows():
# 		if row[histogram_col_name] > 0: macd_hist_colors.append('green')
# 		else:                               macd_hist_colors.append('red')
	
# 	axes_macd.plot (share_df.index, share_df[macd_col_name],          label="macd")
# 	axes_macd.bar(  share_df.index, share_df[histogram_col_name] * 3, label="hist",   color=macd_hist_colors)
# 	axes_macd.plot( share_df.index, share_df[signal_col_name],        label="signal")
# 	axes_macd.set_title('MACD on ' + column_name + ' Column')
# 	axes_macd.legend()																											 # TODO - Rob check out if this is what we need


