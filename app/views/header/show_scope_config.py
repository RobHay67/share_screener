# from tickers.scope.view. import show_page_dataframes
# from app.scope.views.


from screener.scope.view.trial_config import show_scope_trials
from screener.scope.view.strategy_config import show_strategy_config
from charts.scope.views.chart_config import show_scope_chart

import streamlit as st


def show_scope_config(scope):
	page = scope.config['display']
	print(page)
	if scope.page[page]['render']['app_scope']:

		match page:
			case 'screener':
				print('Render the app Scope for this page')
				show_scope_trials(scope)
				show_strategy_config(scope)
			case 'chart':
				print('This is done')
				st.header(':red[Still need to show the overlays config]') #TODO
				show_scope_chart(scope)

		
			# case ''
			# case ''
			# case ''


		# scope_config(scope)