


path = 'path'
title = 'title'
icon = 'icon'
default = 'default'


page_schema = {
	"chart"			:{
		title:"Charting",
		icon:"📊",
		default:False,
		path:"charts/views/page_charts.py"
		}, 
	'intraday'		:{
		title:"Intra Day",
		icon:"🌤️",
		default:False,
		path:"intraday/views/page_intraday.py"
		},  
	'volume'		:{
		title:"Volume",
		icon:"🔊",
		default:False,
		path:"volume/views/page_volume.py"
		}, 
	'research'		:{
		title:"Research",
		icon:"🕵",
		default:False,
		path:"research/views/page_research.py"
		}, 
	'screener'		:{
		title:"Screener",
		icon:"🧪",
		default:False,
		path:"screener/views/page_screener.py"
		}, 
	'websites'		:{
		title:"Websites",
		icon:"🌐",
		default:False,
		path:"websites/views/page_websites.py"
		}, 
	'ticker_index'	:{
		title:"Ticker Index",
		icon:"🗄️",
		default:False,
		path:"ticker_index/scope/views/page_ticker_index.py"
		}, 
	'config'		:{
		title:"Config",
		icon:"⚙️",
		default:False,
		path:"config/views/page_config.py"
		}, 
	'logout'		:{
		title:"Logout",
		icon:"🔒",
		default:True,
		path:"users/views/page_logout.py"
		},  
	'testing'		:{
		title:"Testing",
		icon:"🔬",
		default:False,
		path:"app/views/page_test.py"
		}, 
}

