
from pages.view.home_page import view_project_welcome
from config.view.config_page import view_scope
from charts.views.primary import view_primary
from charts.views.secondary import view_secondary

from analysis.single import analysis_ticker_page
from analysis.research import analysis_research_page
from analysis.intraday import analysis_intraday_page
from analysis.volume import analysis_volume_page
from analysis.multi import  analysis_multi_page


def view_selected_page(scope):
	
	page = scope.page_to_display
	# print( 'Rendering > ', page)
	
	page_map = {
						'home_page'			:view_project_welcome,
						'single'			:analysis_ticker_page,
						'intraday'			:analysis_intraday_page,
						'volume'			:analysis_volume_page,
						'research'			:analysis_research_page,
						'multi'				:analysis_multi_page,
						'charts_primary'	:view_primary,
						'charts_secondary'	:view_secondary,
						'scope'				:view_scope,
					}

	if page in list(page_map.keys()):
		page_map[page](scope)





