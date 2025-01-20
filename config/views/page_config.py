import streamlit as st

from app.views.header.controller import show_page_header
from config.views.button_config import show_config_buttons
from app.scope.views.app import show_app_config
from files.scope.view.files import show_files_config
from app.scope.views.pages import show_page_config 
from tickers.scope.view.config import show_ticker_general_config
from tickers.scope.view.config import show_ticker_config
from users.scope.view.users import show_scope_users
from tickers.scope.view.y_finance import show_y_finance_config
# Config for Screener Page
from screener.scope.view.trial_config import show_trial_general_config
from screener.scope.view.trial_config import show_trial_user_settings
from screener.scope.view.trial_config import show_trial_verdicts
from screener.scope.view.strategy_config import show_strategy_config
# Config for Charts Page
from charts.scope.views.config import show_chart_config
from charts.scope.views.config import show_chart_user_settings


# Page Configuration
page = 'config'
page_title = 'Application Configuration & Settings'
page_icon = '⚙️'
# -----------------------------
scope = st.session_state
scope.config['display'] = page

show_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	show_config_buttons(scope)
	config_page = scope.config['display_scope']['config_page']
	if config_page != None:
		if config_page == 'show_app_config':show_app_config(scope)
		if config_page == 'show_files_config':show_files_config(scope)
		# if button == 'show_ticker_index':has its own page,
		if config_page == 'show_page_config':show_page_config(scope)
		if config_page == 'show_ticker_general_config':show_ticker_general_config(scope)
		if config_page == 'show_ticker_config':show_ticker_config(scope)
		if config_page == 'show_y_finance_config':show_y_finance_config(scope)
		if config_page == 'show_scope_users':show_scope_users(scope)
		
		# Page Specific Config
		if config_page == 'show_trial_config':
			show_trial_general_config(scope)
			show_trial_user_settings(scope)
			show_trial_verdicts(scope)
		if config_page == 'show_strategy_config':
			show_strategy_config(scope)
		if config_page == 'show_chart_config':
			show_chart_config(scope)
			show_chart_user_settings(scope)
		st.divider()
	



