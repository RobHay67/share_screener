import streamlit as st

from app.views.header.controller import show_page_header
from app.views.config.page.buttons import show_config_buttons
from app.views.config.app import show_app_config
from app.views.config.files import show_files_config
from app.views.config.pages import show_page_config 
from app.views.config.tickers.config import show_ticker_general_config
from app.views.config.tickers.missing import show_missing_ticker_config
from app.views.config.users import show_user_config
from app.views.config.y_finance import show_y_finance_config
# Config for Screener Page
from app.views.config.trials import show_trial_general_config
from app.views.config.trials import show_trial_user_settings
from app.views.config.trials import show_trial_verdicts
from app.views.config.strategy import show_strategy_config
# Config for Charts Page
from app.views.config.charts import show_chart_config
from app.views.config.charts import show_chart_user_settings


# Page Configuration
page = 'config'
page_title = 'Application Configuration & Settings'
page_icon = '⚙️'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page

show_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	show_config_buttons(scope)

	config_page = scope.pages['render_config']
	if config_page != None:
		if config_page == 'show_app_config':show_app_config(scope)
		if config_page == 'show_files_config':show_files_config(scope)
		# if button == 'show_ticker_index':has its own page,
		if config_page == 'show_page_config':show_page_config(scope)
		if config_page == 'show_ticker_general_config':show_ticker_general_config(scope)
		if config_page == 'show_missing_ticker_config':show_missing_ticker_config(scope)
		if config_page == 'show_y_finance_config':show_y_finance_config(scope)
		if config_page == 'show_user_config':show_user_config(scope)
		
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
	



