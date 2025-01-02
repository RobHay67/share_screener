import streamlit as st


from app.views.header.controller import render_page_header
from config.views.buttons_config import show_config_buttons
from config.views.app_config import show_app_config
from config.views.file_config import show_files_config
from config.views.page_config import show_page_config 
from config.views.ticker_config import show_ticker_config
from config.views.ticker_config import show_missing_ticker_config
from config.views.user_config import show_user_config
from config.views.y_finance_config import show_y_finance_config

# Config for Screener Page
from config.views.trial_config import show_trial_general_config
from config.views.trial_config import show_trial_user_settings
from config.views.trial_config import show_trial_verdicts
from screener.views.settings.user_strategy import show_strategy_config

# Config for Charts Page
from config.views.chart_config import show_chart_config
from config.views.chart_config import show_chart_user_settings


# Config > app_config  		DONE						all fields reported
# Files						DONE						all fields reported
# Ticker_Index				N/A > seperate module		n/a
# Tickers					DONE						all fields reported			Check Page
# - tickers_missing			DONE						all fields reported	
# - yf						DONE						all fields reported	
# Pages						DONE
# - charts
# - trials
# - strategy
# Users						DONE						all fields reported	




# Page Configuration
page = 'config'
page_title = 'Application Configuration & Settings'
page_icon = '⚙️'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


render_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	show_config_buttons(scope)

	config_page = scope.pages['render_config']
	if config_page != None:
		if config_page == 'show_app_config':show_app_config(scope)
		if config_page == 'show_files_config':show_files_config(scope)
		# if button == 'show_ticker_index':has its own page,
		if config_page == 'show_page_config':show_page_config(scope)
		if config_page == 'show_ticker_config':show_ticker_config(scope)
		if config_page == 'show_missing_ticker_config':show_missing_ticker_config(scope)
		if config_page == 'show_y_finance_config':show_y_finance_config(scope)
		if config_page == 'show_user_config':show_user_config(scope)
		# Page Specific Config
		if config_page == 'show_trial_global_config':
			show_trial_general_config(scope)
			show_trial_user_settings(scope)
			show_trial_verdicts(scope)
		if config_page == 'show_strategy_config':
			show_strategy_config(scope)
		if config_page == 'show_chart_config':
			show_chart_config(scope)
			show_chart_user_settings(scope)
		st.divider()
	



