import streamlit as st

from pages.header.controller import render_app_header
from pages.chart.schema import create_schema_for_plotly
from pages.chart.main_chart import add_main_chart 
from pages.chart.child_charts import add_child_charts
from pages.chart.main_chart import format_main_chart


# Page Configuration
page = 'chart'
page_title = 'Daily Charting'
page_icon = '📊'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page

render_app_header(scope, page_title, page_icon)

if scope.users['logged_in']:

	ticker = scope.pages[page]['selectors']['ticker']

	if ticker in scope.pages[page]['tickers_used_by_page']:

		chart_df		= scope.tickers[ticker][page]['df']
		schema 			= create_schema_for_plotly(scope)
		
		if schema['no_of_charts'] > 0:
			
			fig = add_main_chart(schema)
			fig = add_child_charts(scope, fig, chart_df, schema )
			fig = format_main_chart(scope, fig)
			
			st.plotly_chart(fig, use_container_width=True)

