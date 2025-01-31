import logging
import streamlit as st

from page.header.controller import add_page_header
from charts.helpers.plotly_schema import create_schema_for_plotly
from charts.main_chart import add_main_chart 
from charts.child_charts import add_child_charts
from charts.main_chart import format_main_chart


# Page Configuration
scope = st.session_state
page = 'chart'
scope.display['page'] = page
logging.info("page = charts")

add_page_header(scope)

if scope.users['logged_in']:
	ticker = scope.page[page]['selectors']['ticker']
	if ticker in scope.page[page]['loaded_ticker_list']:
		chart_df 	= scope.tickers[ticker][page]['df']
		schema		= create_schema_for_plotly(scope)
		if schema['no_of_charts'] > 0:
			fig = add_main_chart(schema)
			fig = add_child_charts(scope, fig, chart_df, schema )
			fig = format_main_chart(scope, fig)
			
			st.plotly_chart(fig, use_container_width=True)

