import logging
import streamlit as st


def sidebar_navigation(scope):
	logging.debug("sidebar_navigation")
	screener_page = st.Page(
		page=scope.config['page_schema']['screener']['path'],
		title=scope.config['page_schema']['screener']['title'],
		icon=scope.config['page_schema']['screener']['icon'],
		default=scope.config['page_schema']['screener']['default']
		)
	charting_page = st.Page(
		page=scope.config['page_schema']['chart']['path'],
		title=scope.config['page_schema']['chart']['title'],
		icon=scope.config['page_schema']['chart']['icon'],
		default=scope.config['page_schema']['chart']['default']
		)
	intra_day_page 	= st.Page(
		page=scope.config['page_schema']['intraday']['path'],
		title=scope.config['page_schema']['intraday']['title'],
		icon=scope.config['page_schema']['intraday']['icon'],
		default=scope.config['page_schema']['intraday']['default']
		)
	volume_page = st.Page(
		page=scope.config['page_schema']['volume']['path'],
		title=scope.config['page_schema']['volume']['title'],
		icon=scope.config['page_schema']['volume']['icon'],
		default=scope.config['page_schema']['volume']['default']
		)
	research_page = st.Page(
		page=scope.config['page_schema']['research']['path'],
		title=scope.config['page_schema']['research']['title'],
		icon=scope.config['page_schema']['research']['icon'],
		default=scope.config['page_schema']['research']['default']
		)
	websites_page = st.Page(
		page=scope.config['page_schema']['websites']['path'],
		title=scope.config['page_schema']['websites']['title'],
		icon=scope.config['page_schema']['websites']['icon'],
		default=scope.config['page_schema']['websites']['default']
		)
	ticker_index_page = st.Page(
		page=scope.config['page_schema']['ticker_index']['path'],
		title=scope.config['page_schema']['ticker_index']['title'],
		icon=scope.config['page_schema']['ticker_index']['icon'],
		default=scope.config['page_schema']['ticker_index']['default']
		)
	logout_page = st.Page(
		page=scope.config['page_schema']['logout']['path'],
		title=scope.config['page_schema']['logout']['title'],
		icon=scope.config['page_schema']['logout']['icon'],
		default=scope.config['page_schema']['logout']['default']
		)
	scope_page = st.Page(
		page=scope.config['page_schema']['scope']['path'],
		title=scope.config['page_schema']['scope']['title'],
		icon=scope.config['page_schema']['scope']['icon'],
		default=scope.config['page_schema']['scope']['default']
		)
	testing_page = st.Page(
		page=scope.config['page_schema']['testing']['path'],
		title=scope.config['page_schema']['testing']['title'],
		icon=scope.config['page_schema']['testing']['icon'],
		default=scope.config['page_schema']['testing']['default']
		)

	page_navigation = st.navigation(
		{
		"Research & Analysis"	: [
			screener_page, 
			charting_page, 
			intra_day_page,
			volume_page, 
			research_page, 
			websites_page
			],
		"Config"	: [
			ticker_index_page, 
			scope_page, 
			logout_page, 
			testing_page
			],
		}
	)
	return page_navigation