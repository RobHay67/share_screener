import streamlit as st

from apps.config.three_cols import three_cols
import streamlit as st


from apps.chart.config.primary import render_primary_charts_config
from apps.chart.config.overlays import render_overlays_config
from apps.screener.config.controller import render_available_trials
from strategies.config import render_strategies



def render_config_and_settings(scope):

	app = scope.apps['display_app']

	if scope.apps[app]['render']['app_config'] == True:
		render_page_config(scope)

	if scope.apps[app]['render']['chart_settings'] == True:
		render_primary_charts_config(scope)

	if scope.apps[app]['render']['overlay_settings'] == True:
		render_overlays_config(scope)

	if scope.apps[app]['render']['trial_settings'] == True:
		render_available_trials(scope)

	if scope.apps[app]['render']['strategy'] == True:
		render_strategies(scope)


def view_app_page_config(scope):
	st.subheader('App / Page Configuration - applies to all apps/pages')
	three_cols( 'App / Page  Configuration stored in', {}, 'scope.apps', widget_type='string' )
	three_cols( 'Application List', scope.apps['app_list'], 'scope.apps.app_list', widget_type='string' )
	three_cols( 'App / Page to Display', scope.apps['display_app'], 'scope.apps.display_app', widget_type='string' )
	three_cols( 'Row Limit for Page', scope.apps['row_limit'], 'scope.apps.row_limit', widget_type='string' )
	three_cols( 'Streamlit Latest Button Pressed', scope.apps['button_for_scope'], 'scope.apps.button_for_scope' )


def render_page_config(scope):

	st.write('---')
	
	view_app_page_config(scope)

	app = scope.apps['display_app']
	st.write('---')
	st.subheader( 'Configuration for ' + app.upper() + ' app / page')
	three_cols( 'App / Page Specific Configuration stored in', {}, 'scope.apps['+app+']', widget_type='string' )
	
	st.caption('Lists and Dictionaries')
	three_cols( 'Search Results'  , scope.apps[app]['search_results'], 'scope.apps['+ app +"]['search_results']"    , widget_type='string' )
	three_cols( 'Worklist - current target(s) for page', scope.apps[app]['worklist'], 'scope.apps['+ app +"]['worklist']"    , widget_type='string' )
	three_cols( 'Tickers with Added Columns'   , scope.apps[app]['tickers_with_add_cols'], 'scope.apps['+ app +"]['tickers_with_add_cols", widget_type='string' )
	
	st.caption('Selectors')
	three_cols( 'Market'  , scope.apps[app]['selectors']['market']    , 'scope.apps.'+ app +"['selectors']['market']"    , widget_type='string' )
	three_cols( 'Industry', scope.apps[app]['selectors']['industries'], 'scope.apps.'+ app +"['selectors']['industries']", widget_type='string' )
	three_cols( 'Tickers' , scope.apps[app]['selectors']['tickers']   , 'scope.apps.'+ app +"['selectors']['tickers']"   , widget_type='string' )
	three_cols( 'Ticker'  , scope.apps[app]['selectors']['ticker']    , 'scope.apps.'+ app +"['selectors']['ticker']"    , widget_type='string' )
	
	st.caption('Render')
	three_cols( 'Verdicts ????'  , scope.apps[app]['render']['verdicts']    , 'scope.apps.'+ app +"['render']['verdicts']"    , widget_type='string' )
	three_cols( 'Show Ticker DFs'  , scope.apps[app]['render']['ticker_file']    , 'scope.apps.'+ app +"['render']['ticker_file']"    , widget_type='string' )
	three_cols( 'Show Chart Settings'  , scope.apps[app]['render']['chart_settings']    , 'scope.apps.'+ app +"['render']['chart_config']"    , widget_type='string' )
	three_cols( 'Show Overlay Settings'  , scope.apps[app]['render']['overlay_settings']    , 'scope.apps.'+ app +"['render']['overlay_config']"    , widget_type='string' )
	three_cols( 'Show Trial Settings'  , scope.apps[app]['render']['trial_settings']    , 'scope.apps.'+ app +"['render']['trial_config']"    , widget_type='string' )
	three_cols( 'Show Strategies'  , scope.apps[app]['render']['strategy']    , 'scope.apps.'+ app +"['render']['strategy']"    , widget_type='string' )
	three_cols( 'Show App Config (this page)'  , scope.apps[app]['render']['app_config']    , 'scope.apps.'+ app +"['render']['app_config']"    , widget_type='string' )

	st.write('---')
	st.header('Data Management')
	three_cols( 'Ticker Data and Status Stored in', {}, 'scope.tickers[ticker]', widget_type='string' )
	three_cols( 'Loaded DF File', {}, 'scope.tickers[ticker]' + "['df']", widget_type='string' )

	if app == 'screener':
		st.write('---')
		st.subheader('Test Results (Trial Verdicts) - only for Screener page')
		st.caption('Indiviual Ticker Test Results')
		for ticker in list(scope.tickers.keys()):
			st.subheader(ticker)
			three_cols( 'Overall Test Result (all test must pass)', scope.tickers[ticker][app]['verdict'], "scope.tickers["+ ticker + "]["+app+"['verdict']", widget_type='string' )
			three_cols( 'Do we need to update the verdict', scope.tickers[ticker][app]['replace_verdict'], "scope.tickers["+ ticker + "]["+app+"['replace_verdict']", widget_type='string' )
			three_cols( 'Individual Test (Trial) Results', scope.tickers[ticker][app]['trials'], "scope.tickers["+ ticker + "]["+app+"['trials']", widget_type='string' )
		

	st.write('---')
	st.subheader('Dataframe Status')
	st.caption('What Data needs replacing or recalculating')
	three_cols( 'Dataframe Status Stored in ', {}, 'scope.tickers[ticker][app]', widget_type='string' )
	for ticker in list(scope.tickers.keys()):
		st.subheader(ticker)
		three_cols( 'Replace this DF entirely ?'  , scope.tickers[ticker][app]['replace_df']    , 'scope.tickers['+ ticker + '][' + app + "]['replace_df']"    , widget_type='string' )
		three_cols( 'Type of Column Adder required ='  , scope.tickers[ticker][app]['type_col_adder']    , 'scope.tickers['+ ticker + '][' + app + "]['type_col_adder']"    , widget_type='string' )
		three_cols( 'Which Columns require replacement ?'  , scope.tickers[ticker][app]['column_adders']    , 'scope.tickers['+ ticker + '][' + app + "]['column_adders']", widget_type='string' )


	st.write('---')

