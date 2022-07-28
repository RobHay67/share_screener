
from apps.home_page import render_home_page
from apps.single.controller import render_single_ticker_page
from apps.research.controller import render_research_page
from apps.intraday.controller import render_intraday_page
from apps.volume.controller import render_volume_page
from apps.screener.controller import render_screener_page
from apps.websites.controller import render_websites
from config.charts.primary_config import render_primary_charts_config
from config.charts.secondary_config import render_secondary_charts_config
from apps.scope.controller import render_scope_categories

from users.view.login import render_login_form



def render_selected_app(scope):
	
	page = scope.pages['display_page']
	print( 'Rendering > ', page)
	
	page_map = {
						'login'				:render_login_form,
						'home_page'			:render_home_page,
						
						'single'			:render_single_ticker_page,
						'intraday'			:render_intraday_page,
						'volume'			:render_volume_page,
						'research'			:render_research_page,
						'screener'			:render_screener_page,
						'websites'			:render_websites,
						'charts_primary'	:render_primary_charts_config,
						'charts_secondary'	:render_secondary_charts_config,
						'scope'				:render_scope_categories,
						
					}

	if page in list(page_map.keys()):
		page_map[page](scope)





