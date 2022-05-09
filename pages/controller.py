
from pages.home_page import render_project_welcome
from pages.single.controller import render_single_ticker_page
from pages.research.controller import render_research_page
from pages.intraday.controller import render_intraday_page
from pages.volume.controller import render_volume_page
from pages.screener.controller import render_screener_page
from config.charts.primary_config import render_primary_charts_config
from config.charts.secondary_config import render_secondary_charts_config
from pages.settings.view.settings import render_scope_settings

def render_selected_page(scope):
	
	page = scope.pages['display_page']
	print( 'Rendering > ', page)
	
	page_map = {
						'home_page'			:render_project_welcome,
						'single'			:render_single_ticker_page,
						'intraday'			:render_intraday_page,
						'volume'			:render_volume_page,
						'research'			:render_research_page,
						'screener'			:render_screener_page,
						'charts_primary'	:render_primary_charts_config,
						'charts_secondary'	:render_secondary_charts_config,
						'scope'				:render_scope_settings,
					}

	if page in list(page_map.keys()):
		page_map[page](scope)





