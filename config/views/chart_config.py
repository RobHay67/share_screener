import streamlit as st
from app.views.widgets.cols_three import three_cols


def show_chart_config(scope):

	with st.expander("Chart Settings", expanded=False):
		three_cols( 'Chart Configuration stored in', 		{}, 'scope.charts', widget_type='string' )
		three_cols( 'Chart Config Dictionaries stored in', 	{}, "scope.charts['user_config']", widget_type='string' )

		st.divider()
		three_cols( 'Height (all active charts)', 	scope.charts['total_height'], 	"scope.charts['total_height']" )
		three_cols( 'Height (single chart)', 		scope.charts['primary_height'], "scope.charts['primary_height']" )
		three_cols( 'Chart Colours', 				scope.charts['colours'], 		"scope.charts['colours']" )
		
		st.divider()
		three_cols( 'List of Every Chart', 				scope.charts['chart_list'], 		"scope.charts['chart_list']" )
		three_cols( 'Active Chart List',				scope.charts['active_list'], 		"scope.charts['active_list']" )
		three_cols( 'Charts that require extra Columns',scope.charts['template_col_adders'], "scope.charts['template_col_adders']" )


def show_chart_user_settings(scope):
	with st.expander("User Settings", expanded=False):
		for chart in scope.charts['user_config'].keys():
			#Limit to only overlays
			if scope.charts['user_config'][chart]['is_overlay'] == True:
				three_cols( chart, scope.charts['user_config'][chart], "scope.charts['user_config']["+chart+"]", widget_type='string' )
