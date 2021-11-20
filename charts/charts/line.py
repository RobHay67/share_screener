

import streamlit as st
from plotly.subplots import make_subplots



from analysis.charts.options import render_chart_options


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Line Chart
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
def plot_line_chart(share_data):
	st.markdown('##### Line Chart')

	# show = render_radio_options(33)
	show = render_chart_options(33, show_col_checkboxes=True)

	if show['volume'] == 'Show': show['columns']['volume'] = 'LightSkyBlue'

	fig = make_subplots(specs=[[{"secondary_y": True}]])

	x_data = share_data['date']
	for col_name, col_colour in show['columns'].items():
		if col_name != 'volume'	: plot_type, secondary = go.Scatter	, True
		else					: plot_type, secondary = go.Bar		, False

		fig.add_trace(plot_type(
									x = x_data,
									y 		= share_data[col_name],
									name	= col_name,
									marker_color = col_colour,
								), secondary_y=secondary)
	
	if show['weekends'] == 'Hide':
		fig.update_xaxes(rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}])

	fig.update_layout(height=800)

	st.plotly_chart(fig, use_container_width=True)









def old_plot_basic_chart(scope):
	import plotly.graph_objects as go
	st.markdown('##### Chart of all available data') 

	ticker = scope.selected['research']['ticker_list'][0]

	if ticker in list(scope.ticker_data_files.keys()):
		share_data = scope.ticker_data_files[ticker]
		fig = go.Figure(
				data=go.Scatter(x=share_data['date'], y=share_data['close'])
			)
		fig.update_layout(
			title={
				'text': "Stock Prices Over Past ??????? Years",
				'y':0.9,
				'x':0.5,
				'xanchor': 'center',
				'yanchor': 'top'})
		st.plotly_chart(fig, use_container_width=True)
		st.warning('ROB to change chart to candlestick and maybe add a widget for the date range')
	else:
		st.error('Load and/or Download Share Data to see the chart')