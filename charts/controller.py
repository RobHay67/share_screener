import streamlit as st

from charts.plotly.plotly_schema import create_plotly_schema
from charts.plotly.main_plot import create_main_plot 
from charts.plotly.sub_plot import add_subplot
from charts.plotly.main_plot import format_main_plot


def plot_charts(scope, ticker):
	page 			= scope.page_to_display
	chart_df		= scope.pages[page]['chart_df'][ticker]
	plotly_schema 	= create_plotly_schema(scope)
	if plotly_schema['no_of_charts'] > 0:
		
		fig = create_main_plot(plotly_schema)
		
		fig = add_subplot(scope, fig, chart_df, plotly_schema )
		
		fig = format_main_plot(scope, fig, ticker)
		
		st.plotly_chart(fig, use_container_width=True)



