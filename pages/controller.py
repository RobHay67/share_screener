
from pages.view.home_page import view_project_welcome
from config.view.config_page import view_scope
from charts.view.primary import view_primary
from charts.view.secondary import view_secondary
from screener.view.metrics import view_metrics

from single.controller import view_single_ticker_page
from research.controller import view_research_page
from intraday.controller import view_intraday_page
from volume.controller import view_volume_page
from screener.controller import  view_ticker_screener


def render_selected_page(scope):
	
	page = scope.page_to_display
	# print( 'Rendering > ', page)
	
	page_map = {
						'home_page'			:view_project_welcome,
						'single'			:view_single_ticker_page,
						'intraday'			:view_intraday_page,
						'volume'			:view_volume_page,
						'research'			:view_research_page,
						'screener'			:view_ticker_screener,
						'charts_primary'	:view_primary,
						'charts_secondary'	:view_secondary,
						'metrics'			:view_metrics,
						'scope'				:view_scope,
					}

	if page in list(page_map.keys()):
		page_map[page](scope)





