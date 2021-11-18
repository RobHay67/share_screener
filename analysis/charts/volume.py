
import plotly.graph_objects as go




def plot_volume(fig, chart_title, plot_df, row_no, col_no):
	# Colour the bars on the chart
	colors = ['green' if row['open'] - row['close'] >= 0 else 'red' for index, row in plot_df.iterrows()]
	
	fig.add_trace(	go.Bar(
							x=plot_df['date'],
							y=plot_df['volume'],
							marker_color=colors
							), 
					row=row_no, 
					col=col_no
					)
	fig.update_yaxes(title_text=chart_title, row=row_no, col=col_no)


