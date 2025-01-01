

import streamlit as st



def active_chart_or_test_dropdown(scope):

	page = scope.pages['display']
	
	if page in ['screener', 'chart']:

		widget_key = 'widget_' + page + '_active_list_dropdown'
		widget_label = 'Active '

		if page == 'screener':
			active_list = scope.trials['active_list']
			widget_label = widget_label+'Tests = '+str(len(active_list))
		if page =='chart':
			active_list = scope.charts['active_list']
			widget_label = widget_label+'Charts = '+str(len(active_list))

		st.selectbox(
				label		=widget_label, 
				options		=active_list,
				key			=widget_key,
				)


