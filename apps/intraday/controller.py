# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

import streamlit as st
from apps.app_header.controller import render_app_header


def render_intraday_page(scope):

	app = scope.apps['display_app']

	render_app_header(scope, '🌤️ Intra Day Analysis')

	ticker = scope.apps[app]['selectors']['ticker']

	st.error('TODO render_intraday_page')


	if ticker != 'select a ticker' :		
		
		if ticker in list(scope.tickers.keys()):

			st.error('TODO render_intraday_page')


