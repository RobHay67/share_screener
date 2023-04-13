
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# https://plotly.com/python/range-slider/
# https://plotly.com/python/custom-buttons/



def add_main_chart(schema):
	fig = go.Figure()
	fig = make_subplots(
						rows				= schema['no_of_charts'], 
						cols				= 1, 
						shared_xaxes		= True,
						vertical_spacing	= 0.01, 
						row_heights			= schema['chart_heights']		
						)
	return fig


def format_main_chart(scope, fig):
	# format the overall chart layout
	page 	= scope.display_page
	ticker 	= scope.pages[page]['selectors']['ticker']
	
	fig.update_layout(	
						height 		= scope.charts['total_height'],
						# width		= 1200, 									# let streamlit take care of this
						showlegend	= False, 									# Not Possible to have individual legends per subplot
						margin		= go.layout.Margin(l=20, r=20, b=20, t=35),

						# title={
						# 		'text'		:  ticker,
						# 		'font_color': 'blue',
						# 		'font_size'	: 25,
						# 		'y'			: 1,
						# 		'x'			: 0.5,
						# 		'xanchor'	: 'center',
						# 		'yanchor'	: 'top'
						# 		},
						font={
								'size'		: 14,
								'color'		: 'green',
						},

						yaxis={
								'side'					: 'left',
						},


						xaxis={
								'type' 					: 'date',
								'side'					: 'top',
								'rangeslider_visible'	: False,
								'rangebreaks'			: [{ 'pattern': 'day of week', 'bounds': [6, 1]}],						# Hide Weekends
								# 'rangebreaks'			: [{ 'pattern': 'hour', 'bounds':[23,11]}]),								# this may come in handy later
								'rangeselector' 		: {
															'buttons':[
																		{'count':7,  'label':'7 days'	,  'step':'day'	 , 'stepmode':'backward'},
																		{'count':14, 'label':'14 days'	,  'step':'day'	 , 'stepmode':'backward'},
																		{'count':1,  'label':'1 m'		,  'step':'month', 'stepmode':'backward'},
																		{'count':2,  'label':'2 m'		,  'step':'month', 'stepmode':'backward'},
																		{'count':3,  'label':'3 m'		,  'step':'month', 'stepmode':'backward'},
																		{'count':4,  'label':'4 m'		,  'step':'month', 'stepmode':'backward'},
																		{'count':5,  'label':'5 m'		,  'step':'month', 'stepmode':'backward'},
																		{'count':6,  'label':'6 m'		,  'step':'month', 'stepmode':'backward'},															
																		{'count':1,  'label':'1 y'		,  'step':'year' , 'stepmode':'backward'},
																		{'count':2,  'label':'2 y'		,  'step':'year' , 'stepmode':'backward'},
																		{'count':5,  'label':'5 y'		,  'step':'year' , 'stepmode':'backward'},
																		{'step':'all'},
																	]
														},
						},

					)

	return fig





