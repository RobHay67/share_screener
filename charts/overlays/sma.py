
import plotly.graph_objects as go




def sma_plot(scope, fig, overlay, chart_df, row_no, col_no):

	line_colour = scope.config['charts'][overlay]['plot']['colour']

	fig.add_trace(go.Scatter(
								x		= chart_df['date'], 
								y		= chart_df[overlay], 
								opacity	= 0.7, 
								line	= {
											'color':line_colour, 
											'width':2
											}, 
								name	= overlay,
								showlegend = True,
								
							), 
					row		= row_no, 
					col		= col_no
				)




