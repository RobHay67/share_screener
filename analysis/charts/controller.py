from typing import Sized
import plotly.graph_objects as go
from plotly.subplots import make_subplots


import streamlit as st


def render_selected_charts(scope, ticker):
	chart_df		= scope.selected[scope.display_page]['chart_df'][ticker]
	plotly_schema 	= create_plotly_schema(scope)
	if plotly_schema['no_of_charts'] > 0:
		fig = create_plotly_fig(plotly_schema)
		fig = add_sub_plot_to_fig(scope, fig, chart_df, plotly_schema )
		fig = format_plotly_fig_layout(scope, fig, ticker)
		fig = hide_weekend(fig)		
		st.plotly_chart(fig, use_container_width=True)



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chart Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def create_plotly_schema(scope):
	plotly_schema = {
			'no_of_charts'			: 0,
			'col_no' 				: 1,
			'chart_heights' 		: [],
			'requested_charts' 		: [],
			'requested_overlays'	: [],
	}

	# Based on the User Selections - construct lists and variables of objects that need rendering
	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True and scope.charts[chart]['overlay'] == False: 			# Charts - Selected (active) and IS NOT an overlay
			plotly_schema['no_of_charts'] = plotly_schema['no_of_charts'] + 1
			plotly_schema['chart_heights'].append(scope.charts[chart]['plot']['height'])
			plotly_schema['requested_charts'].append(chart)
		elif  scope.charts[chart]['active'] == True and scope.charts[chart]['overlay'] == True:			# Overlays - Selected (active) and IS an overlay
			plotly_schema['requested_overlays'].append(chart)	


	plotly_schema = make_chart_heights_proportional(plotly_schema)

	return plotly_schema

def make_chart_heights_proportional(plotly_schema):
	relative_total = sum(plotly_schema['chart_heights'])

	for pos, relative_height in enumerate(plotly_schema['chart_heights']):
		proportional_height = relative_height / relative_total
		plotly_schema['chart_heights'][pos] = proportional_height

	return plotly_schema

def create_plotly_fig(plotly_schema):
	fig = go.Figure()
	fig = make_subplots(
						rows				= plotly_schema['no_of_charts'], 
						cols				= 1, 
						shared_xaxes		= True,
						vertical_spacing	= 0.01, 
						row_heights			= plotly_schema['chart_heights']		
						)
	return fig

def add_sub_plot_to_fig(scope, fig, chart_df, plotly_schema):
	for chart_no, chart in enumerate(plotly_schema['requested_charts']):
		print('Adding > ', chart)
		row_no = chart_no+1 
		col_no = plotly_schema['col_no']
		scope.charts[chart]['plot']['function'](scope, fig, chart, chart_df, row_no, col_no)	# add sub_plot
		fig = format_sub_plot(scope, fig, chart, row_no, col_no )
		
		for overlay in plotly_schema['requested_overlays']:
			scope.charts[overlay]['plot']['function'](fig, overlay, chart_df, row_no, col_no)

	return fig

def format_sub_plot(scope, fig, chart, row_no, col_no):

	sub_plot_title = scope.charts[chart]['plot']['title']
	yaxis_format = scope.charts[chart]['plot']['yaxis']

	print('yaxis_format = ', yaxis_format)

	fig.update_yaxes( 
					title_text	= sub_plot_title, 
					tickformat	= yaxis_format,  
					side 		= 'right',
					row			= row_no, 
					col			= col_no,
					
					
					)
	return fig

def format_plotly_fig_layout(scope, fig, ticker):
	# format the overall chart layout
	fig.update_layout(	
						title={
								'text'		:  ticker,
								'font_color': 'blue',
								'font_size'	: 25,
								'y'			: 1,
								'x'			: 0.5,
								'xanchor'	: 'center',
								'yanchor'	: 'top'
								},
						height=scope.chart_height, 
						# width=1200, 
						showlegend=False, 
						xaxis_rangeslider_visible=False,
						margin=go.layout.Margin(l=20, r=20, b=20, t=35)
						# xaxis_rangebreaks=[dict(values=dt_breaks)]		# Removes anny dates without data - but i need to test this
						)

	return fig

def hide_weekend(fig):
	# Hide Weekends
	fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])
	return fig





# =========================================================================================
# Spare Code Snippets TODO - work out what these do exactly
# =========================================================================================

# Format time x Axis
# fig.update_xaxes(rangebreaks=[{ 'pattern': 'hour', 'bounds':[23,11]}])			# this may come in handy later



# define dates with missing values
# dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]

# showgrid ??
# fig.update_yaxes(title_text="MACD", showgrid=False, row=3, col=1)



# def remove_empty_dates(fig, share_df):
# 	# removing all empty dates
# 	dt_all = pd.date_range(start=share_df.index[0],end=share_df.index[-1])				# build complete timeline from start date to end date
# 	dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(share_df.index)]			# retrieve the dates that ARE in the original datset
# 	dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]	# define dates with missing values
# 	fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
# 	return fig



# Format the X Axis							
# fig.update_xaxes(showgrid=False)
# Format the Y Axis
# fig.update_yaxes(showgrid=False)
# fig.update_yaxes(autorange=True) 

# Buttons
# fig.update_layout(
# 				# title_text="Candlestick",
# 				height=800,
# 				yaxis_tickformat='$,.2f',
# 				updatemenus=[dict(
# 						type = "buttons",
# 						direction = "left",
# 						# https://plotly.com/python/range-slider/
# 						# https://plotly.com/python/custom-buttons/
# 						buttons=list([
# 							dict(
# 								args=["type", "surface"],
# 								label="Hide Weekends",
# 								method="restyle"
# 								),
# 							dict(
# 								args=["type", "heatmap"],
# 								label="Show Weekends",
# 								method="restyle"
# 								)]),
# 						pad={"r": 10, "t": 10},
# 						showactive=True,
# 						x=0.11,
# 						xanchor="left",
# 						y=1.1,
# 						yanchor="top"
# 					),],
# 				xaxis=dict(
# 					rangeselector=dict(
# 						buttons=list([
# 							dict(count=1, label="1m",  step="month", stepmode="backward"),
# 							dict(count=6, label="6m",  step="month", stepmode="backward"),
# 							dict(count=1, label="YTD", step="year",  stepmode="todate"),
# 							dict(count=1, label="1y",  step="year",  stepmode="backward"),
# 							dict(step="all")
# 						])),
# 					rangeslider=dict( visible=True ),
# 					type="date",
# 					),
				
# 				yaxis2_tickformat=',.',
				
# 				showlegend=False,
# 				)
