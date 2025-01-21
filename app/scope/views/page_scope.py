import streamlit as st

from app.views.header.controller import show_page_header
from app.scope.views.set_config_group import show_config_group_selection_buttons

from app.scope.views.config_summary import show_scope_summary
from app.scope.views.config_config import show_scope_config
from files.scope.view.config_files import show_scope_files
from app.scope.views.config_pages import show_scope_page 
from ticker_index.scope.views.config_ticker_index import show_scope_ticker_index
from tickers.scope.view.config_tickers import show_scope_tickers
from tickers.scope.view.config_ticker_schema import show_scope_tickers_schema
from users.scope.view.config_users import show_scope_users
from tickers.scope.view.config_yf import show_scope_yf
from charts.scope.views.config_chart import show_scope_chart
# Config for Screener Page
from screener.scope.view.config_trials import show_scope_trials
from screener.scope.view.config_trials import show_trial_verdicts
from screener.scope.view.config_strategy import show_scope_strategy
# Config for Charts Page



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
		case 'show_scope_summary':show_scope_summary(scope)


		case 'show_scope_config':show_scope_config(scope)
		case 'show_scope_files':show_scope_files(scope)
		case 'show_scope_ticker_index':show_scope_ticker_index(scope)
		case 'show_scope_page':show_scope_page(scope)
		case 'show_scope_tickers':show_scope_tickers(scope)
		case 'show_scope_tickers_schema':show_scope_tickers_schema(scope)		
		case 'show_scope_yf':show_scope_yf(scope)
		case 'show_scope_users':show_scope_users(scope)
		# Page Specific Config
		case 'show_scope_chart':show_scope_chart(scope)
		case 'show_trial_config':
			show_scope_trials(scope)
			show_trial_verdicts(scope)
		case 'show_scope_strategy':show_scope_strategy(scope)


