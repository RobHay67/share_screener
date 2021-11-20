
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# https://plotly.com/python/range-slider/
# https://plotly.com/python/custom-buttons/



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

def create_main_plot(plotly_schema):
	fig = go.Figure()
	fig = make_subplots(
						rows				= plotly_schema['no_of_charts'], 
						cols				= 1, 
						shared_xaxes		= True,
						vertical_spacing	= 0.01, 
						row_heights			= plotly_schema['chart_heights']		
						)
	return fig

def format_main_plot(scope, fig, ticker):
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
						height=scope.primary_chart_height, 
						# width=1200, 
						# showlegend=False, 
						xaxis_rangeslider_visible=False,
						margin=go.layout.Margin(l=20, r=20, b=20, t=35),
						
						xaxis_rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}],						# Hide Weekends
						# xaxis_rangebreaks=[{ 'pattern': 'hour', 'bounds':[23,11]}])								# this may come in handy later
						
						xaxis_rangeselector =  {
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
						xaxis_type = "date",
						)

	return fig


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chart Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def make_chart_heights_proportional(plotly_schema):
	relative_total = sum(plotly_schema['chart_heights'])
	for pos, relative_height in enumerate(plotly_schema['chart_heights']):
		proportional_height = relative_height / relative_total
		plotly_schema['chart_heights'][pos] = proportional_height
	return plotly_schema




# =========================================================================================
# Spare Code Snippets TODO - work out what these do exactly
# =========================================================================================

# Buttons
# fig.update_layout(
# 					# updatemenus=[dict(
# 					# 					type = "buttons",
# 					# 					direction = "left",
# 					# 					buttons=list([
# 					# 						dict(
# 					# 							args=["type", "surface"],
# 					# 							label="Hide Weekends",
# 					# 							method="restyle"
# 					# 							),
# 					# 						dict(
# 					# 							args=["type", "heatmap"],
# 					# 							label="Show Weekends",
# 					# 							method="restyle"
# 					# 							)]),
# 					# 					pad={"r": 10, "t": 10},
# 					# 					showactive=True,
# 					# 					x=0.11,
# 					# 					xanchor="left",
# 					# 					y=1.1,
# 					# 					yanchor="top"
# 					# 				),],
# 					)


# def remove_empty_dates(fig, share_df):
# 	# removing all empty dates
# 	dt_all = pd.date_range(start=share_df.index[0],end=share_df.index[-1])				# build complete timeline from start date to end date
# 	dt_obs = [d.strftime("%Y-%m-%d") for d in pd.to_datetime(share_df.index)]			# retrieve the dates that ARE in the original datset
# 	dt_breaks = [d for d in dt_all.strftime("%Y-%m-%d").tolist() if not d in dt_obs]	# define dates with missing values
# 	fig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])
# 	fig.update_layout(xaxis_rangebreaks=[dict(values=dt_breaks)])						# Removes anny dates without data - but i need to test this
# 	return fig