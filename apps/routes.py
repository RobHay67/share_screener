from apps.login.login import render_login_form
from apps.home.home_page import render_home_page
from apps.chart.controller import render_chart_ticker_page
from apps.research.controller import render_research_page
from apps.intraday.controller import render_intraday_page
from apps.volume.controller import render_volume_page
from apps.screener.controller import render_screener_page
from apps.websites.controller import render_websites
from apps.config_charts.primary import render_primary_charts_config
from apps.config_charts.secondary import render_secondary_charts_config
from apps.config_app.controller import render_scope_categories



def render_selected_app(scope):
	
	app = scope.apps['display_app']
	print( 'Rendering > ', app)
	
	page_map = {
						'login'				:render_login_form,
						'home_page'			:render_home_page,
						
						'chart'				:render_chart_ticker_page,
						'intraday'			:render_intraday_page,
						'volume'			:render_volume_page,
						'research'			:render_research_page,
						'screener'			:render_screener_page,
						'websites'			:render_websites,
						
						'charts_primary'	:render_primary_charts_config,
						'charts_secondary'	:render_secondary_charts_config,
						
						'scope'				:render_scope_categories,
						
					}

	if app in list(page_map.keys()):
		page_map[app](scope)





