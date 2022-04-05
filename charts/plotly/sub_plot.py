import plotly.graph_objects as go


def add_subplot(scope, fig, chart_df, plotly_schema):
	for chart_no, chart in enumerate(plotly_schema['add_chart']):
		row_no = chart_no+1 
		col_no = plotly_schema['col_no']

		scope.config['charts']['config'][chart]['plot']['function'](scope, fig, chart, chart_df, row_no, col_no)	# add sub_plot
		fig = format_sub_plot(scope, fig, chart, row_no, 1 )
		
		if scope.config['charts']['config'][chart]['add_overlays'] == True:											# only apply overlays to relevant charts
			for overlay in plotly_schema['add_overlay']:
				scope.config['charts']['config'][overlay]['plot']['function'](scope, fig, overlay, chart_df, row_no, col_no)

	return fig



def format_sub_plot(scope, fig, chart, row_no, col_no):

	sub_plot_title = scope.config['charts']['config'][chart]['plot']['title']
	yaxis_format = scope.config['charts']['config'][chart]['plot']['yaxis']

	fig.update_xaxes(
					showgrid	= False,				# Vertical Lines
					)	

	fig.update_yaxes( 
					title_text	= sub_plot_title, 
					tickformat	= yaxis_format,  
					# side 		= 'left',
					row			= row_no, 
					col			= col_no,
					showgrid	= False,				# Horizontal Lines
					)

	return fig


# showlegend=True, 




# Format the Y Axis
# fig.update_yaxes(autorange=True) 					# i dont beleive this does anything at all
