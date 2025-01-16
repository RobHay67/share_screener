import time

def scope_config(scope):

	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] 	= time.time()
	
	scope.config['page'] = page_config
	user_config_pages(scope)

	scope.config['page_list'] = list(scope.config['page'].keys())
	# scope.config['page_list'] = [ 
	# 							'chart', 
	# 							'intraday', 
	# 							'volume', 
	# 							'research', 
	# 							'screener', 
	# 							'websites', 
	# 							'ticker_index', 
	# 							'config',
	# 							'logout',
	# 							'testing',
	# 							]
	scope.config['display_config_group'] = None

	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['config_ticker'] = ['select a ticker']
	scope.config['dropdowns']['ohlcv_columns'] = ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	


def user_config_pages(scope):
	# These Setting can be changed for each user
	# so we need to be able to call when changing user
	scope.config['row_limit'] = 100
	scope.config['display'] = 'streamlit_app'
	scope.config['share_market'] = 'ASX'
	# scope.config['share_market'] = 'USA'
	scope.config['download_days'] = '5d'


def scope_seach_for_ticker(scope):
	# company names for the ticker search
	scope.config['ticker_search'] = {}
	scope.config['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()




path = 'path'
title = 'title'
icon = 'icon'
default = 'default'


page_config = {
	"chart"			:{title:"Charting"		,icon:"📊", default:False, path:"charts/views/page_charts.py"}, 
	'intraday'		:{title:"Intra Day"		,icon:"🌤️", default:False, path:"intraday/views/page_intraday.py"},  
	'volume'		:{title:"Volume"		,icon:"🔊", default:False, path:"volume/views/page_volume.py"}, 
	'research'		:{title:"Research"		,icon:"🕵", default:False, path:"research/views/page_research.py"}, 
	'screener'		:{title:"Screener"		,icon:"🧪", default:False, path:"screener/views/page_screener.py", }, 
	'websites'		:{title:"Websites"		,icon:"🌐", default:False, path:"websites/views/page_websites.py"}, 
	'ticker_index'	:{title:"Ticker Index"	,icon:"🗄️", default:False, path:"ticker_index/scope/views/page_ticker_index.py"}, 
	'config'		:{title:"Config"		,icon:"⚙️" , default:False, path:"config/views/page_config.py"}, 
	'logout'		:{title:"Logout"		,icon:"🔒", default:True , path:"users/views/page_logout.py"},  
	'testing'		:{title:"Testing"		,icon:"🔬", default:False, path:"app/views/page_test.py"}, 
}

