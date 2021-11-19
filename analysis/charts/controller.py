import plotly.graph_objects as go
from plotly.subplots import make_subplots


import streamlit as st



def render_selected_charts(scope, ticker):

	col_no 		= 1
	chart_df	= scope.selected[scope.display_page]['chart_df'][ticker]

	no_of_charts, requested_charts, requested_overlays, chart_heights = subplot_schema(scope)

	if no_of_charts > 0:
		chart_heights = calc_chart_heights(chart_heights)

		fig = chart_structure(no_of_charts, chart_heights)
		
		for chart_no, chart in enumerate(requested_charts):
			row_no = chart_no+1 
			print(chart)
			scope.charts[chart]['plot']['function'](fig, scope, chart, chart_df, row_no, col_no)
			
			for overlay in requested_overlays:
				scope.charts[overlay]['plot']['function'](fig, overlay, chart_df, row_no, col_no)

		fig = format_chart_layout(scope, fig, ticker)

		# Hide Weekends
		fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])
		st.plotly_chart(fig, use_container_width=True)








# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chart Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def subplot_schema(scope):
	no_of_charts 		= 0
	chart_heights 		= []
	requested_charts 	= []
	requested_overlays 	= []

	# Based on the User Selections - construct lists and variables of objects that need rendering
	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True and scope.charts[chart]['overlay'] == False: 			# Charts - Selected (active) and IS NOT an overlay
			print('Adding > ', chart)
			no_of_charts += 1
			chart_heights.append(scope.charts[chart]['plot']['height'])
			requested_charts.append(chart)
		elif  scope.charts[chart]['active'] == True and scope.charts[chart]['overlay'] == True:			# Overlays - Selected (active) and IS an overlay
			requested_overlays.append(chart)		

	return no_of_charts, requested_charts, requested_overlays, chart_heights 

def calc_chart_heights(chart_heights):
	relative_total = sum(chart_heights)

	for pos, relative_height in enumerate(chart_heights):
		proportional_height = relative_height / relative_total
		chart_heights[pos] = proportional_height

	return chart_heights

def chart_structure(no_of_charts, chart_heights):
	fig = go.Figure()
	fig = make_subplots(
						rows				= no_of_charts, 
						cols				= 1, 
						shared_xaxes		= True,
						vertical_spacing	= 0.01, 
						row_heights			= chart_heights		
						)
	return fig

def format_chart_layout(scope, fig, ticker):
	# format the overall chart and sub_chart layout
	fig.update_layout(	
						title={
								'text': ticker,
								'font_color':'blue',
								'font_size':25,
								'y':1,
								'x':0.5,
								'xanchor': 'center',
								'yanchor': 'top'
								},
						height=scope.chart_height, 
						# width=1200, 
						showlegend=False, 
						xaxis_rangeslider_visible=False,
						margin=go.layout.Margin(l=20, r=20, b=20, t=35)
						# xaxis_rangebreaks=[dict(values=dt_breaks)]
						)

	return fig


# =========================================================================================
# Y Axis Format TODO - move into the individual chart rendering!
# =========================================================================================

# Format the Axis
# fig.update_layout(yaxis_tickformat='$',
#               yaxis2_tickformat='$',
#               yaxis3_tickformat='$',
#               yaxis4_tickformat='$',
#               title_text=Current_Stock_Profile.shortName)
