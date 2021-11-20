
import plotly.graph_objects as go




def volume_plot(scope, fig, chart, chart_df, row_no, col_no):

	# Colour the bars on the chart
	colors = ['green' if row['open'] - row['close'] >= 0 else 'red' for index, row in chart_df.iterrows()]
	
	fig.add_trace(	go.Bar(
							x=chart_df['date'],
							y=chart_df['volume'],
							marker_color=colors
							), 
					row=row_no, 
					col=col_no
					)


