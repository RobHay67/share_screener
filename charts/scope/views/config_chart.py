import streamlit as st
from app.scope.views.buttons.button_choose_scope import scope_button
from app.scope.views.buttons.button_data_type import data_type_button
from app.scope.views.buttons.show_scope_value import show_scope_single_value, show_scope_values
from app.scope.views.buttons.dropdown_choose_scope import scope_dropdown

def show_scope_chart(scope):

	st.divider()
	scope_button(scope, "scope.charts", scope.charts, make_red=True, suffix_only=False)

	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
	with col1:scope_button(scope, "scope.charts['schema']", scope.charts['schema'])
	with col2:scope_button(scope, "scope.charts['chart_list']", scope.charts['chart_list'])
	with col3:scope_button(scope, "scope.charts['active_list']", scope.charts['active_list'])
	with col4:scope_button(scope, "scope.charts['template_col_adders']", scope.charts['template_col_adders'])
	with col5:scope_button(scope, "scope.charts['colours']", scope.charts['colours'])
	with col6:scope_button(scope, "scope.charts['primary_height']", scope.charts['primary_height'])
	with col7:scope_button(scope, "scope.charts['total_height']", scope.charts['total_height'])
	with col8:scope_button(scope, "scope.charts['user_config']", scope.charts['user_config'])
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
	with col6:show_scope_single_value("primary_height", scope.charts['primary_height'])
	with col7:show_scope_single_value("total_height", scope.charts['total_height'])

	scope_button(scope, "scope.charts['user_config'][chart]", scope.charts['user_config'], make_red=True, suffix_only=False)
	chart = scope_dropdown(scope, build_chart_list(scope))

	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns([1,1,1,1,1,1,1,1,1])
	with col1:scope_button(scope, "scope.charts['user_config']["+chart+"]['active']", scope.charts['user_config'][chart]['active'])
	with col2:scope_button(scope, "scope.charts['user_config']["+chart+"]['name']", scope.charts['user_config'][chart]['name'])
	with col3:scope_button(scope, "scope.charts['user_config']["+chart+"]['short_name']", scope.charts['user_config'][chart]['short_name'])
	with col4:scope_button(scope, "scope.charts['user_config']["+chart+"]['is_overlay']", scope.charts['user_config'][chart]['is_overlay'])
	with col5:scope_button(scope, "scope.charts['user_config']["+chart+"]['add_overlays']", scope.charts['user_config'][chart]['add_overlays'])
	with col6:scope_button(scope, "scope.charts['user_config']["+chart+"]['definition']", scope.charts['user_config'][chart]['definition'])
	with col7:scope_button(scope, "scope.charts['user_config']["+chart+"]['notes']", scope.charts['user_config'][chart]['notes'])
	with col8:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']", scope.charts['user_config'][chart]['plot'])	
	with col9:scope_button(scope, "scope.charts['user_config']["+chart+"]['add_columns']", scope.charts['user_config'][chart]['add_columns'])
	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns([1,1,1,1,1,1,1,1,1])
	with col4:show_scope_single_value("is_overlay", scope.charts['user_config'][chart]['is_overlay'])
	with col5:show_scope_single_value("add_overlays", scope.charts['user_config'][chart]['add_overlays'])

	col1,col2 = st.columns([4,4])
	with col1:scope_button(scope, "["+chart+"]['plot']", scope.charts['user_config'][chart]['plot'], make_red=True, suffix_only=False)
	with col2:scope_button(scope, 'Overlays in charts schema ????? Rob to configure', scope.charts['chart_list'], make_red=True, suffix_only=False)
	col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([1,1,1,1,1,1,1,1])
	with col1:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['function']", scope.charts['user_config'][chart]['plot']['function'])
	with col2:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['title']", scope.charts['user_config'][chart]['plot']['title'])
	with col3:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['scale']", scope.charts['user_config'][chart]['plot']['scale'])
	with col4:scope_button(scope, "scope.charts['user_config']["+chart+"]['plot']['yaxis']", scope.charts['user_config'][chart]['plot']['yaxis'])
	with col1:show_scope_single_value("plot_function", scope.charts['user_config'][chart]['plot']['function'])
	with col2:show_scope_single_value("plot_title", scope.charts['user_config'][chart]['plot']['title'])
	with col3:show_scope_single_value("plot_scale", scope.charts['user_config'][chart]['plot']['scale'])
	with col4:show_scope_single_value("plot_yaxis", scope.charts['user_config'][chart]['plot']['yaxis'])



	if scope.config['display_scope']['scope_key'] != None:
		show_scope_values(scope)


def build_chart_list(scope):
	chart_list = []
	for chart, config in scope.charts['schema'].items():
		if scope.charts['schema'][chart]['is_overlay'] == False:
			# print('This chart > ', chart)
			chart_list.append(chart)
	chart_list.sort()
	return chart_list
