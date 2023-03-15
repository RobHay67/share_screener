import streamlit as st

from apps.config_app.three_cols import three_cols




def scope_ticker_search(scope):

	# company names for the ticker search
	scope.ticker_search = {}
	scope.ticker_search = (scope.ticker_index['company_name']).to_dict()




def scope_dropdown_menus(scope):
	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['ohlcv_columns'] 	= ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	



def render_app_config(scope):

	app = scope.apps['display_app']

	st.caption( app + ' specific Lists for App / Page')

	# st.caption('App/Page Specific Lists')
	three_cols( 'Search Results'  , scope.apps[app]['search_results'], 'scope.apps.'+ app +'.search_results'    , widget_type='string' )
	three_cols( 'App Worklist'    , scope.apps[app]['worklist'], 'scope.apps.'+ app +'.worklist'    , widget_type='string' )
	three_cols( 'Mined Tickers'   , scope.apps[app]['mined_tickers'], 'scope.apps.'+ app +'.mined_tickers'    , widget_type='string' )

	st.caption('Selectors')
	three_cols( 'Market'  , scope.apps[app]['selectors']['market']    , 'scope.apps.'+ app +'.selectors.market'    , widget_type='string' )
	three_cols( 'Industry', scope.apps[app]['selectors']['industries'], 'scope.apps.'+ app +'.selectors.industries', widget_type='string' )
	three_cols( 'Tickers' , scope.apps[app]['selectors']['tickers']   , 'scope.apps.'+ app +'.selectors.tickers'   , widget_type='string' )
	three_cols( 'Ticker'  , scope.apps[app]['selectors']['ticker']    , 'scope.apps.'+ app +'.selectors.ticker'    , widget_type='string' )
	
	st.caption('Render Dataframes')
	three_cols( 'Ticker DFs'  , scope.apps[app]['render']['tickers']    , 'scope.apps.'+ app +'.render.tickers'    , widget_type='string' )
	three_cols( 'Chart DFs'  , scope.apps[app]['render']['charts']    , 'scope.apps.'+ app +'.render.charts'    , widget_type='string' )
	three_cols( 'Trial DFs'  , scope.apps[app]['render']['trials']    , 'scope.apps.'+ app +'.render.trials'    , widget_type='string' )
	
	st.caption('Render Configuration')
	three_cols( 'App Config (this page section)'  , scope.apps[app]['render']['config']    , 'scope.apps.'+ app +'.render.config'    , widget_type='string' )
	three_cols( 'Chart Config'  , scope.apps[app]['render']['chart']    , 'scope.apps.'+ app +'.render.chart'    , widget_type='string' )
	three_cols( 'Overlay Config'  , scope.apps[app]['render']['overlay']    , 'scope.apps.'+ app +'.render.overlay'    , widget_type='string' )
	three_cols( 'Strategies'  , scope.apps[app]['render']['strategy']    , 'scope.apps.'+ app +'.render.strategy'    , widget_type='string' )

	st.write('---')
	st.caption('Global Application Configuration - applies to all apps/pages')
	three_cols( 'Application List', scope.apps['app_list'], 'scope.apps.app_list', widget_type='string' )
	three_cols( 'App to Display', scope.apps['display_app'], 'scope.apps.display_app', widget_type='string' )
	three_cols( 'Row Limit for Page', scope.apps['row_limit'], 'scope.apps.row_limit', widget_type='string' )
	three_cols( 'Streamlit Latest Button Pressed', scope.apps['button_for_scope'], 'scope.apps.button_for_scope' )
	st.write('---')



