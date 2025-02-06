import logging
from tickers.scope.view.config_vedicts import show_config_verdicts
from trials.scope.view.config_trials import show_config_trials
from trials.scope.view.config_strategy import show_config_strategy
from charts.scope.views.config_charts import show_config_charts
from ticker_index.scope.views.config_ticker_index import show_config_ticker_index
from config.views.config_pages import show_config_pages
from tickers.scope.view.config_tickers import show_config_tickers


def router_show_requested_config(scope):
	logging.debug("router_show_requested_config")
	page = scope.display['page']
	config_to_show = scope.page[page]['show']['config']

	match config_to_show:
		case 'Page Config':show_config_pages(scope)
		case 'Ticker Data':show_config_tickers(scope)
		case 'ticker_index':show_config_ticker_index(scope)
		case 'Charts':show_config_charts(scope)
		case 'Verdicts':show_config_verdicts(scope)
		case 'Trials':show_config_trials(scope)
		case 'Strategies':show_config_strategy(scope)	
