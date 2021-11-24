import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from charts.main_plot import create_plotly_schema, create_main_plot, format_main_plot
from charts.sub_plot import add_subplot





def view_charts(scope, ticker):
	chart_df		= scope.pages[scope.display_page]['chart_df'][ticker]
	plotly_schema 	= create_plotly_schema(scope)
	if plotly_schema['no_of_charts'] > 0:
		fig = create_main_plot(plotly_schema)
		fig = add_subplot(scope, fig, chart_df, plotly_schema )
		fig = format_main_plot(scope, fig, ticker)
		st.plotly_chart(fig, use_container_width=True)



