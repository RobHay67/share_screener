import plotly.graph_objects as go


def add_subplot(scope, fig, chart_df, plotly_schema):
	for chart_no, chart in enumerate(plotly_schema['requested_charts']):
		print('Adding > ', chart)
		row_no = chart_no+1 
		col_no = plotly_schema['col_no']

		print( 'Chart =  ', chart, 'Row = ', row_no, ' Col_no = ', col_no)

		scope.charts[chart]['plot']['function'](scope, fig, chart, chart_df, row_no, col_no)	# add sub_plot			# TODO - uncomment after testing

		# For Testing Purposes only
		# from charts.charts.candlestick import candle_plot																# TODO - REMOVE AFTER TESTING
		# from charts.charts.macd import macd_plot																		# TODO - REMOVE AFTER TESTING
		# candle_plot(scope, fig, chart, chart_df, row_no, 1)															# TODO - REMOVE AFTER TESTING
		# macd_plot(scope, fig, chart, chart_df, row_no, col_no)														# TODO - REMOVE AFTER TESTING

		fig = format_sub_plot(scope, fig, chart, row_no, 1 )
		
		# for overlay in plotly_schema['requested_overlays']:															# TODO - uncomment after testing
		# 	scope.charts[overlay]['plot']['function'](scope, fig, overlay, chart_df, row_no, col_no)					# TODO - uncomment after testing

	return fig

def format_sub_plot(scope, fig, chart, row_no, col_no):

	sub_plot_title = scope.charts[chart]['plot']['title']
	yaxis_format = scope.charts[chart]['plot']['yaxis']

	fig.update_xaxes(
					showgrid	= False,				# Vertical Lines
					)	

	fig.update_yaxes( 
					title_text	= sub_plot_title, 
					tickformat	= yaxis_format,  
					side 		= 'left',
					row			= row_no, 
					col			= col_no,
					showgrid	= True,				# Horizontal Lines
					)

	return fig


# showlegend=True, 




# Format the Y Axis
# fig.update_yaxes(autorange=True) 					# i dont beleive this does anything at all
