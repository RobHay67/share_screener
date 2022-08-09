
import plotly.graph_objects as go


def add_child_charts(scope, fig, chart_df, schema):

	for chart_no, chart in enumerate(schema['add_chart']):
		row_no = chart_no+1 
		col_no = schema['col_no']

		# add sub_plot
		scope.charts['config'][chart]['plot']['function'](scope, fig, chart, chart_df, row_no, col_no)
		fig = format_child_chart(scope, fig, chart, row_no, 1 )
		
		# only apply overlays to relevant charts
		if scope.charts['config'][chart]['add_overlays'] == True:											
			for overlay in schema['add_overlay']:
				scope.charts[overlay]['plot']['function'](scope, fig, overlay, chart_df, row_no, col_no)

	return fig



def format_child_chart(scope, fig, chart, row_no, col_no):

	sub_plot_title = scope.charts['config'][chart]['plot']['title']
	yaxis_format = scope.charts['config'][chart]['plot']['yaxis']

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

