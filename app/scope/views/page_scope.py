import streamlit as st

from app.views.header.controller import show_page_header
from app.scope.views.set_config_group import show_config_group_selection_buttons

from app.scope.views.app import show_app_config
from files.scope.view.files import show_files_config
from app.scope.views.pages import show_scope_page 
from tickers.scope.view.config import show_ticker_general_config
from tickers.scope.view.config import show_scope_tickers
from users.scope.view.users import show_scope_users
from tickers.scope.view.y_finance import show_y_finance_config
# Config for Screener Page
from screener.scope.view.trial_config import show_scope_trials
from screener.scope.view.trial_config import show_trial_verdicts
from screener.scope.view.strategy_config import show_strategy_config
# Config for Charts Page
from charts.scope.views.chart_config import show_scope_chart


# Page Configuration
page = 'scope'
page_title = 'Application Configuration & Settings'
page_icon = '⚙️'
# -----------------------------
scope = st.session_state
scope.config['display'] = page

show_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	show_config_group_selection_buttons(scope)
	config_page = scope.config['display_scope']['config_page']

	match config_page:
		case 'show_app_config':show_app_config(scope)
		case 'show_files_config':show_files_config(scope)
		# case 'show_ticker_index':has its own page,
		case 'show_scope_page':show_scope_page(scope)
		case 'show_ticker_general_config':show_ticker_general_config(scope)
		case 'show_scope_tickers':show_scope_tickers(scope)
		case 'show_y_finance_config':show_y_finance_config(scope)
		case 'show_scope_users':show_scope_users(scope)
		# Page Specific Config
		case 'show_scope_chart':show_scope_chart(scope)
		case 'show_trial_config':
			show_scope_trials(scope)
			show_trial_verdicts(scope)
		case 'show_strategy_config':show_strategy_config(scope)


