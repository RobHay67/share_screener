

import plotly.graph_objects as go




# line_cols - No Additional Columns are required to render the Line Chart




def line_plot(scope, fig, chart, chart_df, row_no, col_no):

	# column 	= scope.config['charts']['config'][chart]['metrics']['column']
	colors = ['yellow', 'green', 'red', 'blue']
	#         open        high    low    close
	columns = scope.config['dropdowns']['price_columns ']
	
	for pos, column in enumerate(columns):

		fig.add_trace( go.Scatter(
								x		= chart_df['date'],
								y		= chart_df[column],
								name 	= column,
								visible = True,
								line	= dict(color=colors[pos], width=2),
								), 
					row=row_no, 
					col=col_no,
					)	
		

		# The below was adding buttons - but not correctly
		# um = [ {} for _ in range(len(columns)) ]
		# buttons = []
		# menuadjustment = 0.15

		# buttonX = -0.1
		# buttonY = 1 + menuadjustment
		# for i, col in enumerate(columns):
		# 	button = dict(method='restyle',
		# 				label=col,
		# 				visible=True,
		# 				args=[{'visible':True,
		# 						'line.color' : colors[i]}, [i]],
		# 				args2 = [{'visible': False,
		# 							'line.color' : colors[i]}, [i]],
		# 				)
			
		# 	# adjust some button features
		# 	buttonY = buttonY-menuadjustment
		# 	um[i]['buttons'] = [button]
		# 	um[i]['showactive'] = False
		# 	um[i]['y'] = buttonY
		# 	um[i]['x'] = buttonX

		# # add a button to toggle all traces on and off
		# button2 = dict(method='restyle',
		# 			label='All',
		# 			visible=True,
		# 			args=[{'visible':True}],
		# 			args2 = [{'visible': False}],
		# 			)
		# # assign button2 to an updatemenu and make some adjustments
		# um.append(dict())
		# um[i+1]['buttons'] = [button2]
		# um[i+1]['showactive'] = True
		# um[i+1]['y']=buttonY - menuadjustment
		# um[i+1]['x'] = buttonX
			
		# # add dropdown menus to the figure
		# fig.update_layout(showlegend=True, updatemenus=um)

		# # adjust button type
		# for m in fig.layout.updatemenus:
		# 	m['type'] = 'buttons'

		# # f = fig.full_figure_for_development(warn=False)
		# # fig.show()







# # create figure
# fig = go.Figure()

# # Add surface trace
# fig.add_trace(go.Surface(z=df.values.tolist(), colorscale="Viridis"))

# # Update plot sizing
# fig.update_layout(
#     width=800,
#     height=900,
#     autosize=False,
#     margin=dict(t=0, b=0, l=0, r=0),
#     template="plotly_white",
# )

# # Update 3D scene options
# fig.update_scenes(
#     aspectratio=dict(x=1, y=1, z=0.7),
#     aspectmode="manual"
# )

# # Add dropdown
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type = "buttons",
#             direction = "left",
#             buttons = list([ 
# 							dict(args=["type", "surface"],label="3D Surface", method="restyle"),
#                 			dict(args=["type", "heatmap"],label="Heatmap"   , method="restyle")
#             			]),
#             pad={"r": 10, "t": 10},
#             showactive=True,
#             x=0.11,
#             xanchor="left",
#             y=1.1,
#             yanchor="top"
#         ),
#     ]
# )

# # Add annotation
# fig.update_layout(
#     annotations=[
#         dict(text="Trace type:", showarrow=False,
#                              x=0, y=1.08, yref="paper", align="left")
#     ]
# )

# fig.show()
