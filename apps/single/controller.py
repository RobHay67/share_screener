import streamlit as st

from apps.ticker_loader.header import render_page_title
# from charts.controller import plot_charts
from apps.ticker_loader.controller import render_ticker_loader


from apps.single.plotly_schema import create_plotly_schema
from apps.single.main_plot import create_main_plot 
from apps.single.sub_plot import add_subplot
from apps.single.main_plot import format_main_plot

from apps.ticker_loader.search_results import render_search_results
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_single_ticker_page(scope):
	
	render_page_title(scope, 'Ticker Analysis (single ticker)')

	render_ticker_loader(scope)

	ticker = scope.apps['single']['selectors']['ticker']

	if ticker != 'select a ticker' :
		
		# Check that we have data available for this ticker
		# before attempting to make any plots

		if ticker in scope.apps['single']['dfs'].keys():	
			app 			= scope.apps['display_app']
			ticker 			= scope.apps[app]['selectors']['ticker']
			chart_df		= scope.apps[app]['dfs'][ticker]
			plotly_schema 	= create_plotly_schema(scope)
			
			if plotly_schema['no_of_charts'] > 0:
				
				fig = create_main_plot(plotly_schema)
				
				fig = add_subplot(scope, fig, chart_df, plotly_schema )
				
				fig = format_main_plot(scope, fig)
				
				st.plotly_chart(fig, use_container_width=True)

	else:
		render_search_results(scope)

		

