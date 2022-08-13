import streamlit as st

from partials.ticker_loader.header import render_page_title
from partials.ticker_loader.controller import render_ticker_loader

from apps.single.schema import create_schema_for_plotly
from apps.single.chart_main import add_main_chart 
from apps.single.chart_children import add_child_charts
from apps.single.chart_main import format_main_chart

from partials.ticker_search.search_results import render_search_results
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_single_ticker_page(scope):
	
	render_page_title(scope, 'Ticker Analysis (single ticker)')

	render_ticker_loader(scope)


	if len(scope.apps['single']['search_results']) == 0:

		ticker = scope.apps['single']['selectors']['ticker']

		if ticker != 'select a ticker' :
			
			app 			= scope.apps['display_app']
			ticker 			= scope.apps[app]['selectors']['ticker']
			chart_df		= scope.tickers[ticker]['apps'][app]['df']
			schema 			= create_schema_for_plotly(scope)
			
			if schema['no_of_charts'] > 0:
				
				fig = add_main_chart(schema)
				
				fig = add_child_charts(scope, fig, chart_df, schema )
				
				fig = format_main_chart(scope, fig)
				
				st.plotly_chart(fig, use_container_width=True)

	else:
		render_search_results(scope)

		

