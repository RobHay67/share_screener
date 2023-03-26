import streamlit as st

from apps.config_app.three_cols import three_cols
from apps.config_app.charts import view_charts_config
from apps.config_app.trials import view_trials_config



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



def render_page_config(scope):

	app = scope.apps['display_app']

	st.caption( app + ' specific Lists for App / Page')

	# st.caption('App/Page Specific Lists')
	three_cols( 'Search Results'  , scope.apps[app]['search_results'], 'scope.apps.'+ app +'.search_results'    , widget_type='string' )
	three_cols( 'App Worklist'    , scope.apps[app]['worklist'], 'scope.apps.'+ app +'.worklist'    , widget_type='string' )
	three_cols( 'Tickers with Added Columns'   , scope.apps[app]['tickers_with_add_cols'], 'scope.apps.'+ app +'.tickers_with_add_cols'    , widget_type='string' )

	st.caption('Selectors')
	three_cols( 'Market'  , scope.apps[app]['selectors']['market']    , 'scope.apps.'+ app +'.selectors.market'    , widget_type='string' )
	three_cols( 'Industry', scope.apps[app]['selectors']['industries'], 'scope.apps.'+ app +'.selectors.industries', widget_type='string' )
	three_cols( 'Tickers' , scope.apps[app]['selectors']['tickers']   , 'scope.apps.'+ app +'.selectors.tickers'   , widget_type='string' )
	three_cols( 'Ticker'  , scope.apps[app]['selectors']['ticker']    , 'scope.apps.'+ app +'.selectors.ticker'    , widget_type='string' )
	
	st.caption('Render Dataframes')
	three_cols( 'Ticker DFs'  , scope.apps[app]['render']['ticker_file']    , 'scope.apps.'+ app +'.render.ticker_file'    , widget_type='string' )
	three_cols( 'Chart DFs'  , scope.apps[app]['render']['col_added_df']    , 'scope.apps.'+ app +'.render.col_added_df'    , widget_type='string' )
	
	st.caption('Render Configuration')
	three_cols( 'Chart Settings'  , scope.apps[app]['render']['chart_settings']    , 'scope.apps.'+ app +'.render.chart_config'    , widget_type='string' )
	three_cols( 'Overlay Settings'  , scope.apps[app]['render']['overlay_settings']    , 'scope.apps.'+ app +'.render.overlay_config'    , widget_type='string' )
	three_cols( 'Trial Settings'  , scope.apps[app]['render']['trial_settings']    , 'scope.apps.'+ app +'.render.trial_config'    , widget_type='string' )
	three_cols( 'Strategies'  , scope.apps[app]['render']['strategy']    , 'scope.apps.'+ app +'.render.strategy'    , widget_type='string' )
	three_cols( 'App Config (this page)'  , scope.apps[app]['render']['app_config']    , 'scope.apps.'+ app +'.render.app_config'    , widget_type='string' )

# scope.apps.chart.tickers_with_add_cols 
	st.write('---')
	st.caption('Render Ticker Status')
	for ticker in list(scope.tickers.keys()):
		# if ticker in scope.apps[app]['tickers_with_add_cols']:
		st.subheader(ticker)
		three_cols( 'Replace DF?'  , scope.tickers[ticker][app]['replace_df']    , 'scope.tickers['+ ticker + '][' + app + '].replace_df'    , widget_type='string' )
		three_cols( 'Column Adder Type'  , scope.tickers[ticker][app]['type_col_adder']    , 'scope.tickers['+ ticker + '][' + app + '].type_col_adder'    , widget_type='string' )
		st.write('scope.tickers['+ticker+'['+app+'].column_adders')
		st.write(scope.tickers[ticker][app]['column_adders'])


	# for app in scope.apps['app_list']:
	# 	# add a key for each app
	# 	scope.tickers[ticker][app] = {}
	# 	# add a 'df' key to house the app dataframe
	# 	# and other df and column management information
	# 	scope.tickers[ticker][app]['df'] = {}
	# 	scope.tickers[ticker][app]['replace_df'] = True
	# 	scope.tickers[ticker][app]['type_col_adder'] = None   # 'charts' or 'trials'
	# 	scope.tickers[ticker][app]['column_adders'] = {}






	st.write('---')
	st.caption('Global Application Configuration - applies to all apps/pages')
	three_cols( 'Application List', scope.apps['app_list'], 'scope.apps.app_list', widget_type='string' )
	three_cols( 'App to Display', scope.apps['display_app'], 'scope.apps.display_app', widget_type='string' )
	three_cols( 'Row Limit for Page', scope.apps['row_limit'], 'scope.apps.row_limit', widget_type='string' )
	three_cols( 'Streamlit Latest Button Pressed', scope.apps['button_for_scope'], 'scope.apps.button_for_scope' )
	st.write('---')

	# Add in the User config
	if app == 'chart':
		view_charts_config(scope)

	if app == 'screener':
		view_trials_config(scope)

