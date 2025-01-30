path = 'path'
title = 'title'
icon = 'icon'
default = 'default'


page_schema = {
	'welcome'		:{
		title:"Welcome",
		icon:"🔒",
		default:True,
		path:"users/page_welcome.py"
		},  
	'logout'		:{
		title:"Logout",
		icon:"🔒",
		default:True,
		path:"users/page_logout.py"
		},  
	"chart"			:{
		title:"Charting",
		icon:"📊",
		default:False,
		path:"charts/page_charts.py"
		}, 
	'intraday'		:{
		title:"Intra Day",
		icon:"🌤️",
		default:False,
		path:"intraday/page_intraday.py"
		},  
	'volume'		:{
		title:"Volume",
		icon:"🔊",
		default:False,
		path:"volume/page_volume.py"
		}, 
	'research'		:{
		title:"Research",
		icon:"🕵",
		default:False,
		path:"research/page_research.py"
		}, 
	'screener'		:{
		title:"Screener",
		icon:"🧪",
		default:False,
		path:"screener/page_screener.py"
		}, 
	'websites'		:{
		title:"Websites",
		icon:"🌐",
		default:False,
		path:"websites/page_websites.py"
		}, 
	'ticker_index'	:{
		title:"Ticker Index",
		icon:"🗄️",
		default:False,
		path:"ticker_index/page_ticker_index.py"
		}, 
	'scope'		:{
		title:"Scope",
		icon:"⚙️",
		default:False,
		path:"config/page_scope.py"
		}, 
	'testing'		:{
		title:"Testing",
		icon:"🔬",
		default:False,
		path:"page/page_test.py"
		}, 
}
