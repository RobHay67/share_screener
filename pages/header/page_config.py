import streamlit as st
from pages.config.three_cols import three_cols
from pages.chart.settings.controller import render_available_charts
from pages.chart.settings.overlays import render_overlays_config
from pages.screener.settings.controller import render_available_trials
from strategies.config import render_strategies



def render_config_and_settings(scope):

	page = scope.display_page

	if scope.pages[page]['render']['app_config'] == True:
		render_page_config(scope)

	if scope.pages[page]['render']['chart_settings'] == True:
		render_available_charts(scope)

	if scope.pages[page]['render']['overlay_settings'] == True:
		render_overlays_config(scope)

	if scope.pages[page]['render']['trial_settings'] == True:
		render_available_trials(scope)

	if scope.pages[page]['render']['strategy'] == True:
		render_strategies(scope)


def view_app_page_config(scope):
	st.subheader('Page Configuration - applies to all pages')
	three_cols( 'Page  Configuration stored in', {}, 'scope.pages', widget_type='string' )
	three_cols( 'Application List', scope.pages['page_list'], 'scope.pages.app_list', widget_type='string' )
	three_cols( 'Page to Display', scope.display_page, 'scope.pages.display_app', widget_type='string' )
	three_cols( 'Row Limit for Page', scope.pages['row_limit'], 'scope.pages.row_limit', widget_type='string' )
	three_cols( 'Streamlit Latest Button Pressed', scope.pages['button_for_scope'], 'scope.pages.button_for_scope' )


def render_page_config(scope):

	st.write('---')
	
	view_app_page_config(scope)

	page = scope.display_page
	st.write('---')
	st.subheader( 'Configuration for ' + page.upper() + ' Page')
	three_cols( 'Page Specific Configuration stored in', {}, 'scope.pages['+page+']', widget_type='string' )
	
	st.caption('Lists and Dictionaries')
	three_cols( 'Search Results'  , scope.pages[page]['search_results'], 'scope.pages['+ page +"]['search_results']"    , widget_type='string' )
	three_cols( 'Worklist - current target(s) for page', scope.pages[page]['worklist'], 'scope.pages['+ page +"]['worklist']"    , widget_type='string' )
	three_cols( 'Tickers with Added Columns'   , scope.pages[page]['tickers_with_add_cols'], 'scope.pages['+ page +"]['tickers_with_add_cols", widget_type='string' )
	
	st.caption('Selectors')
	three_cols( 'Market'  , scope.pages[page]['selectors']['market']    , 'scope.pages.'+ page +"['selectors']['market']"    , widget_type='string' )
	three_cols( 'Industry', scope.pages[page]['selectors']['industries'], 'scope.pages.'+ page +"['selectors']['industries']", widget_type='string' )
	three_cols( 'Tickers' , scope.pages[page]['selectors']['tickers']   , 'scope.pages.'+ page +"['selectors']['tickers']"   , widget_type='string' )
	three_cols( 'Ticker'  , scope.pages[page]['selectors']['ticker']    , 'scope.pages.'+ page +"['selectors']['ticker']"    , widget_type='string' )
	
	st.caption('Render')
	three_cols( 'Show Ticker DFs'  , scope.pages[page]['render']['ticker_file']    , 'scope.pages.'+ page +"['render']['ticker_file']"    , widget_type='string' )
	three_cols( 'Show Chart Settings'  , scope.pages[page]['render']['chart_settings']    , 'scope.pages.'+ page +"['render']['chart_config']"    , widget_type='string' )
	three_cols( 'Show Overlay Settings'  , scope.pages[page]['render']['overlay_settings']    , 'scope.pages.'+ page +"['render']['overlay_config']"    , widget_type='string' )
	three_cols( 'Show Trial Settings'  , scope.pages[page]['render']['trial_settings']    , 'scope.pages.'+ page +"['render']['trial_config']"    , widget_type='string' )
	three_cols( 'Show Strategies'  , scope.pages[page]['render']['strategy']    , 'scope.pages.'+ page +"['render']['strategy']"    , widget_type='string' )
	three_cols( 'Show page Config (this page)'  , scope.pages[page]['render']['app_config']    , 'scope.pages.'+ page +"['render']['app_config']"    , widget_type='string' )

	st.write('---')
	st.header('Data Management')
	three_cols( 'Ticker Data and Status Stored in', {}, 'scope.tickers[ticker]', widget_type='string' )
	three_cols( 'Loaded DF File', {}, 'scope.tickers[ticker]' + "['df']", widget_type='string' )

	if page == 'screener':
		st.write('---')
		st.subheader('Test Results (Trial Verdicts) - only for Screener page')
		st.caption('Indiviual Ticker Test Results')
		for ticker in list(scope.tickers.keys()):
			st.subheader(ticker)
			three_cols( 'Overall Test Result (all test must pass)', scope.tickers[ticker][page]['verdict'], "scope.tickers["+ ticker + "]["+page+"['verdict']", widget_type='string' )
			three_cols( 'Do we need to update the verdict', scope.tickers[ticker][page]['replace_verdict'], "scope.tickers["+ ticker + "]["+page+"['replace_verdict']", widget_type='string' )
			three_cols( 'Individual Test (Trial) Results', scope.tickers[ticker][page]['trials'], "scope.tickers["+ ticker + "]["+page+"['trials']", widget_type='string' )
		

	st.write('---')
	st.subheader('Dataframe Status')
	st.caption('What Data needs replacing or recalculating')
	three_cols( 'Dataframe Status Stored in ', {}, 'scope.tickers[ticker][page]', widget_type='string' )
	for ticker in list(scope.tickers.keys()):
		st.subheader(ticker)
		three_cols( 'Replace this DF entirely ?'  , scope.tickers[ticker][page]['replace_df']    , 'scope.tickers['+ ticker + '][' + page + "]['replace_df']"    , widget_type='string' )
		three_cols( 'Type of Column Adder required ='  , scope.tickers[ticker][page]['type_col_adder']    , 'scope.tickers['+ ticker + '][' + page + "]['type_col_adder']"    , widget_type='string' )
		three_cols( 'Which Columns require replacement ?'  , scope.tickers[ticker][page]['column_adders']    , 'scope.tickers['+ ticker + '][' + page + "]['column_adders']", widget_type='string' )


	st.write('---')

