from apps.login.login import render_login_form
from apps.home.home_page import render_home_page
from apps.chart.controller import render_chart_ticker_page
from apps.research.controller import render_research_page
from apps.intraday.controller import render_intraday_page
from apps.volume.controller import render_volume_page
from apps.screener.controller import render_screener_page
from apps.websites.controller import render_websites
from apps.index.controller import render_ticker_index_page
from apps.config.controller import render_scope_categories



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

						'index'				:render_ticker_index_page,
												
						'scope'				:render_scope_categories,
						
					}

	if app in list(page_map.keys()):
		page_map[app](scope)





