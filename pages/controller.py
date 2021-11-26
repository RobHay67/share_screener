
from pages.view.home_page import view_project_welcome
from config.view.config_page import view_scope
from charts.views.primary import view_primary
from charts.views.secondary import view_secondary
from analysis.controller import single_ticker_analysis, intraday_analysis, volume_analysis, research_analysis, multi_tickers_analysis


def view_selected_page(scope):
	
	page = scope.page_to_display
	# print( 'Rendering > ', page)
	
	page_map = {
						'home_page'			:view_project_welcome,
						'single'			:single_ticker_analysis,
						'intraday'			:intraday_analysis,
						'volume'			:volume_analysis,
						'research'			:research_analysis,
						'multi'				:multi_tickers_analysis,
						'charts_primary'	:view_primary,
						'charts_secondary'	:view_secondary,
						'scope'				:view_scope,
					}

	if page in list(page_map.keys()):
		page_map[page](scope)





