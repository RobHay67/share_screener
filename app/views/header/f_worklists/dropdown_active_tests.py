

import streamlit as st



def active_chart_or_test_dropdown(scope):

	page = scope.config['display']
	
	if page in ['screener', 'chart']:

		widget_key = 'widget_' + page + '_active_list_dropdown'
		widget_label = '('

		if page == 'screener':
			active_list = scope.trials['active_list']
			widget_label = widget_label+str(len(active_list))+') Trials / Tests'
		if page =='chart':
			active_list = scope.charts['active_list']
			widget_label = widget_label+str(len(active_list))+') Charts'

		st.selectbox(
				label		=widget_label, 
				options		=active_list,
				key			=widget_key,
				)


