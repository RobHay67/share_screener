import streamlit as st

from views.header.controller import render_page_header
from charts.views.schema import create_schema_for_plotly
from charts.views.main_chart import add_main_chart 
from charts.views.child_charts import add_child_charts
from charts.views.main_chart import format_main_chart


# Page Configuration
page = 'chart'
page_title = 'Daily Charting'
page_icon = '📊'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page

render_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:

	ticker = scope.pages[page]['selectors']['ticker']

	if ticker in scope.pages[page]['loaded_ticker_list']:

		chart_df		= scope.tickers[ticker][page]['df']
		schema 			= create_schema_for_plotly(scope)
		
		if schema['no_of_charts'] > 0:
			
			fig = add_main_chart(schema)
			fig = add_child_charts(scope, fig, chart_df, schema )
			fig = format_main_chart(scope, fig)
			
			st.plotly_chart(fig, use_container_width=True)

