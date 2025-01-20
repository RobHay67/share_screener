import streamlit as st
from app.views.widgets.cols_three import three_cols
from config.views.button_choose_scope import scope_button
from config.views.button_data_type import data_type_button
from config.views.show_scope_value import show_scope_single_value, show_scope_values


def show_scope_chart(scope):

	st.divider()
	scope_button(scope, "scope.charts", scope.charts, make_red=True, suffix_only=False)

	col1,col2,col3,col4,col5,col6,col7 = st.columns(7)
	with col1:scope_button(scope, "scope.charts['chart_list']", scope.charts['chart_list'])
	with col2:scope_button(scope, "scope.charts['active_list']", scope.charts['active_list'])
	with col3:scope_button(scope, "scope.charts['template_col_adders']", scope.charts['template_col_adders'])
	with col4:scope_button(scope, "scope.charts['colours']", scope.charts['colours'])
	with col5:scope_button(scope, "scope.charts['primary_height']", scope.charts['primary_height'])
	with col6:scope_button(scope, "scope.charts['total_height']", scope.charts['total_height'])
	with col7:scope_button(scope, "scope.charts['user_config']", scope.charts['user_config'])

	chart = next(iter(scope.charts['user_config'].keys()))
	scope_button(scope, "scope.charts['user_config'][chart]", scope.charts['user_config'], make_red=True, suffix_only=False)
	scope_button(scope, '[chart] = '+chart, scope.charts['user_config'][chart], make_red=False, suffix_only=False)

	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns([1,1,1,1,1,1,1,3,1])
	with col1:scope_button(scope, "scope.charts['user_config']["+chart+"]['active']", scope.charts['user_config'][chart]['active'])
	with col2:scope_button(scope, "scope.charts['user_config']["+chart+"]['name']", scope.charts['user_config'][chart]['name'])
	with col3:scope_button(scope, "scope.charts['user_config']["+chart+"]['short_name']", scope.charts['user_config'][chart]['short_name'])
	with col4:scope_button(scope, "scope.charts['user_config']["+chart+"]['is_overlay']", scope.charts['user_config'][chart]['is_overlay'])
	with col5:scope_button(scope, "scope.charts['user_config']["+chart+"]['add_overlays']", scope.charts['user_config'][chart]['add_overlays'])
	with col6:scope_button(scope, "scope.charts['user_config']["+chart+"]['definition']", scope.charts['user_config'][chart]['definition'])
	with col7:scope_button(scope, "scope.charts['user_config']["+chart+"]['notes']", scope.charts['user_config'][chart]['notes'])
	with col8:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']", scope.charts['user_config'][chart]['plot'])	
	with col9:scope_button(scope, "scope.charts['user_config']["+chart+"]['add_columns']", scope.charts['user_config'][chart]['add_columns'])

	col1,col2,col3,col4,col5 = st.columns([7,1,1,1,1])
	# st.write('Plot Title')
	# st.write(scope.charts['user_config'][chart]['plot']['title'])
	# scope_button(scope, "scope.charts['user_config'][candlestick]['plot']['title']", scope.charts['user_config'][chart]['plot'])

	with col2:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['function']", scope.charts['user_config'][chart]['plot']['function'])
	with col3:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['title']", scope.charts['user_config'][chart]['plot']['title'])
	with col4:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['scale']", scope.charts['user_config'][chart]['plot']['scale'])
	with col5:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['yaxis']", scope.charts['user_config'][chart]['plot']['yaxis'])
# {
# "active":true
# "name":"Candlestick"
# "short_name":"Candle"
# "is_overlay":false
# "add_overlays":true
# "definition":"https://www.investopedia.com/terms/c/candlestick.asp"
# "notes":"Open set by he novice trading yesterdays sentiment, High is set by the Bulls, Low is set by the Bears. The close is set by the professional investors."
# "plot":{
# 		"function":"<function candle_plot at 0x11ffd0360>"
# 		"title":"Candlestick"
# 		"scale":1
# 		"yaxis":"$,.2f"
# 		}
# "add_columns":NULL
# }


	# st.divider()
	if scope.config['display_scope']['scope_key'] != None:
		show_scope_values(scope)










	with st.expander("Chart Configuration", expanded=False):
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
