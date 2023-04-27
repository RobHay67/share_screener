import streamlit as st


from pages.config.three_cols import three_cols


def render_scope_charts(scope):

	with st.expander("Chart Settings", expanded=False):
		three_cols( 'Chart Configuration stored in', {}, 'scope.charts', widget_type='string' )
		three_cols( 'Chart Config Dictionaries stored in', {}, "scope.charts['config']", widget_type='string' )

		st.divider()
		three_cols( 'Height (all active charts)', scope.charts['total_height'], "scope.charts['total_height']" )
		three_cols( 'Height (single chart)', scope.charts['primary_height'], "scope.charts['primary_height']" )
		three_cols( 'Chart Colours', scope.charts['colours'], "scope.charts['colours']" )
		
		st.divider()
		three_cols( 'Every Chart and Overlay in Config dictionary', scope.charts['chart_list'], "scope.charts['chart_list']" )
		three_cols( 'Active Chart List', scope.charts['active_list'], "scope.charts['active_list']" )
		three_cols( 'Charts that require extra Column', scope.charts['template_col_adders'], "scope.charts['template_col_adders']" )

	with st.expander("Chart Dictionaries (python code)", expanded=False):
		for chart in scope.charts['config'].keys():
			#Limit to only charts
			if scope.charts['config'][chart]['is_overlay'] == False:
				three_cols( chart, scope.charts['config'][chart], "scope.charts['config']["+chart+"]", widget_type='string' )

	with st.expander("Overlay Dictionaries (python code)", expanded=False):
		for chart in scope.charts['config'].keys():
			#Limit to only overlays
			if scope.charts['config'][chart]['is_overlay'] == True:
				three_cols( chart, scope.charts['config'][chart], "scope.charts['config']["+chart+"]", widget_type='string' )
