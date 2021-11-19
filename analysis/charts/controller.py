import plotly.graph_objects as go
from plotly.subplots import make_subplots


import streamlit as st



def render_selected_charts(scope, ticker):
	
	# Establish Defaults Variables and empty lists
	no_of_charts 			= 0
	relative_row_heights 	= []
	col_no 					= 1
	charts_to_render_list 	= []
	overlays_to_render_list = []
	chart_df 				= scope.selected[scope.display_page]['chart_df'][ticker]

	# Based on the User Selections - construct lists and variables of objects that need rendering
	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True and scope.charts[chart]['overlay'] == False: 			# Charts - Selected (active) and IS NOT an overlay
			print('Adding > ', chart)
			no_of_charts += 1
			relative_row_heights.append(scope.charts[chart]['chart_schema']['height'])
			charts_to_render_list.append(chart)
		elif  scope.charts[chart]['active'] == True and scope.charts[chart]['overlay'] == True:			# Overlays - Selected (active) and IS an overlay
			overlays_to_render_list.append(chart)																				
		
	# Render the selected Charts
	if no_of_charts > 0:
		row_heights = proportional_row_heights(relative_row_heights)
		fig = go.Figure()
		fig = make_subplots(
							rows				= no_of_charts, 
							cols				= 1, 
							shared_xaxes		= True,
							vertical_spacing	= 0.01, 
							row_heights			= row_heights		
							)
		
		# plot requested charts and overlays
		for chart_no, chart in enumerate(charts_to_render_list):
			row_no = chart_no+1 
			chart_title = scope.charts[chart]['chart_schema']['title']
			scope.charts[chart]['chart_schema']['function'](fig, chart_title, chart_df, row_no, col_no)
			
			# Add in Any Overlays to the same chart
			for overlay in overlays_to_render_list:
				scope.charts[overlay]['chart_schema']['function'](fig, overlay, chart_df, row_no, col_no)

		# format the charts
		fig.update_layout(	
							title=ticker,
							height=scope.chart_height, 
							# width=1200, 
							showlegend=False, 
							xaxis_rangeslider_visible=False,
							margin=go.layout.Margin(l=20, r=20, b=20, t=20)
							# xaxis_rangebreaks=[dict(values=dt_breaks)]
							)
		# Hide Weekends
		fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])
		# output to browser
		st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chart Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def proportional_row_heights(relative_row_heights):
	relative_total = sum(relative_row_heights)

	for pos, relative_height in enumerate(relative_row_heights):
		proportional_height = relative_height / relative_total
		relative_row_heights[pos] = proportional_height

	return relative_row_heights


# =========================================================================================
# Y Axis Format TODO - move into the individual chart rendering!
# =========================================================================================

# Format the Axis
# fig.update_layout(yaxis_tickformat='$',
#               yaxis2_tickformat='$',
#               yaxis3_tickformat='$',
#               yaxis4_tickformat='$',
#               height=750,
#               width=1200,
#               showlegend=False,
#               title_text=Current_Stock_Profile.shortName)
