

import streamlit as st



# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Charting Helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_chart_options(unique_key, show_col_checkboxes=False):

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)

	with col1: st.write('Select Options')
	# Options for the chart
	st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: left;}</style>', unsafe_allow_html=True)
	with col2: show_weekends 	= st.radio("weekends", ('Hide','Show'), key=unique_key)
	with col3: show_volume 		= st.radio("volume"  , ('Hide','Show'), key=unique_key)

	# build the list of columns
	columns_to_plot = {}
	if show_col_checkboxes:
		with col4: open = st.checkbox('open', key=unique_key)
		with col5: high = st.checkbox('high', key=unique_key)
		with col6: low = st.checkbox('low', key=unique_key)
		with col7: close = st.checkbox('close', key=unique_key, value=True)
		# with col5: vol = st.checkbox('volume', key=unique_key)

		if open: columns_to_plot['open'] = 'blue'
		if high: columns_to_plot['high'] = 'green'
		if low: columns_to_plot['low'] = 'red'
		if close: columns_to_plot['close'] = 'black'
		# if vol: columns_to_plot['volume'] = 'LightSkyBlue'

	return {'weekends':show_weekends, 'volume':show_volume, 'columns':columns_to_plot }




