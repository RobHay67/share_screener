import streamlit as st


from apps.config_app.three_cols import three_cols



def view_charts_config(scope):
	st.caption('Charts Configuration - Raw Dictionaries and Lists')
	
	three_cols( 'Colours', scope.chart_config['colours'], 'scope.apps.charts.colours' )
	three_cols( 'Total Chart Height', scope.chart_config['total_height'], 'scope.apps.charts.total_height' )
	three_cols( 'Height of Primary Charts', scope.chart_config['primary_height'], 'scope.apps.charts.primary_height' )
	three_cols( 'Chart List', scope.chart_config['chart_list'], 'scope.apps.charts.chart_list' )

	st.markdown("""---""")
	
	for chart in  scope.chart_config['chart_list']:
		st.subheader(chart)
		st.write('scope.config.charts['+chart+']')
		st.write(scope.charts[chart])
