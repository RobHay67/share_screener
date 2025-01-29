
from app.scope.views.config_config import show_config_config
from app.scope.views.config_display import show_config_display
from files.scope.view.config_files import show_config_files
from app.scope.views.config_pages import show_config_pages 
from ticker_index.scope.views.config_ticker_index import show_config_ticker_index
from tickers.scope.view.config_tickers import show_config_tickers
from tickers.scope.view.config_ticker_schema import show_config_tickers_schema
from users.scope.view.config_users import show_config_users
from tickers.scope.view.config_yf import show_config_yf
from tickers.scope.view.config_vedicts import show_config_verdicts
from charts.scope.views.config_charts import show_config_charts
from screener.scope.view.config_trials import show_config_trials
from tickers.scope.view.config_vedicts import show_config_verdicts
from screener.scope.view.config_strategy import show_config_strategy


def route_to_config_page(scope):
	
	config_page = scope.display['config_page']

	match config_page:
		case 'route_config_config':			show_config_config(scope)
		case 'route_config_display':		show_config_display(scope)
		case 'route_config_files':			show_config_files(scope)
		case 'route_config_ticker_index':	show_config_ticker_index(scope)
		case 'route_config_page':			show_config_pages(scope)
		case 'route_config_tickers':		show_config_tickers(scope)
		case 'route_config_tickers_schema':	show_config_tickers_schema(scope)		
		case 'route_config_yf':				show_config_yf(scope)
		case 'route_config_verdicts':		show_config_verdicts(scope)
		case 'route_config_users':			show_config_users(scope)
		case 'route_config_chart':			show_config_charts(scope)
		case 'route_config_trial':			show_config_trials(scope)
		case 'route_config_verdicts':		show_config_verdicts(scope)
		case 'route_config_strategy':		show_config_strategy(scope)



