import streamlit as st

from app.views.header.controller import show_page_header
from charts.helpers.plotly_schema import create_schema_for_plotly
from charts.views.main_chart import add_main_chart 
from charts.views.child_charts import add_child_charts
from charts.views.main_chart import format_main_chart


# Page Configuration
page = 'chart'
page_title = 'Daily Charting'
page_icon = '📊'
# -----------------------------
scope = st.session_state
scope.config['display'] = page

show_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:

	ticker = scope.page[page]['selectors']['ticker']

	if ticker in scope.page[page]['loaded_ticker_list']:

		chart_df		= scope.tickers[ticker][page]['df']
		schema 			= create_schema_for_plotly(scope)
		
		if schema['no_of_charts'] > 0:
			
			fig = add_main_chart(schema)
			fig = add_child_charts(scope, fig, chart_df, schema )
			fig = format_main_chart(scope, fig)
			
			st.plotly_chart(fig, use_container_width=True)

