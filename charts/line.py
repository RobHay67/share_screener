

import streamlit as st
from plotly.subplots import make_subplots



from charts.options import render_chart_options


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




