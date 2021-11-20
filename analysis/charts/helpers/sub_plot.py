import plotly.graph_objects as go


def add_subplot(scope, fig, chart_df, plotly_schema):
	for chart_no, chart in enumerate(plotly_schema['requested_charts']):
		print('Adding > ', chart)
		row_no = chart_no+1 
		col_no = plotly_schema['col_no']
		scope.charts[chart]['plot']['function'](scope, fig, chart, chart_df, row_no, col_no)	# add sub_plot
		fig = format_sub_plot(scope, fig, chart, row_no, col_no )
		
		for overlay in plotly_schema['requested_overlays']:
			scope.charts[overlay]['plot']['function'](scope, fig, overlay, chart_df, row_no, col_no)

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
					side 		= 'right',
					row			= row_no, 
					col			= col_no,
					showgrid	= True,				# Horizontal Lines
					)

	return fig






# Format the Y Axis
# fig.update_yaxes(autorange=True) 					# i dont beleive this does anything at all
