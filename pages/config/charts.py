import streamlit as st


from pages.config.three_cols import three_cols


def view_charts_config(scope):

	st.subheader('Global Chart Configuration')
	three_cols( 'Global Charts Configuration stored in', {}, 'scope.chart_config', widget_type='string' )
	three_cols( 'Every available Chart or Overlay', scope.chart_config['chart_list'], "scope.chart_config['chart_list']" )
	three_cols( 'Total Height for all currently active charts', scope.chart_config['total_height'], "scope.chart_config['total_height']" )
	three_cols( 'Height of a single charts', scope.chart_config['primary_height'], "scope.chart_config['primary_height']" )
	three_cols( 'Available Colours', scope.chart_config['colours'], "scope.chart_config['colours']" )
	three_cols( 'Active Chart List', scope.chart_config['active_list'], "scope.chart_config['active_list']" )
	three_cols( 'Charts which require Column Adders', scope.chart_config['column_adders'], "scope.chart_config['column_adders']" )


	st.write('---')
	st.subheader('Charts Configuration - Raw Configuration Dictionaries')
	three_cols( 'Charts Configuration stored in', {}, 'scope.charts', widget_type='string' )
	for chart in  scope.chart_config['chart_list']:
		three_cols( chart, scope.charts[chart], 'scope.charts['+chart+']', widget_type='string' )
