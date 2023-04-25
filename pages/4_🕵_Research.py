import streamlit as st

from pages.header.controller import render_app_header
from y_finance.metadata import fetch_yfinance_metadata
from pages.research.info import company_general
# from pages.research.info import business_summary
from pages.research.info import fundamental
from pages.research.info import general
from pages.research.info import market_info
from pages.research.dividends import dividends
from pages.research.investors import institutional
from pages.research.investors import major
from pages.research.financials import financial_statements
from pages.research.financials import annual
from pages.research.financials import quarterly
from pages.research.financials import balance_sheet
from pages.research.financials import balance_sheet_qtr
from pages.research.financials import cashflow
from pages.research.financials import cashflow_qtr
from pages.research.financials import earnings
from pages.research.financials import earnings_qtr
from pages.research.calendar import calendar
from pages.research.news import news


# TODO - I like this example from the ASX for CBA - https://www2.asx.com.au/markets/company/cba

# Page Configuration
page = 'research'
page_title = 'Company Research'
page_icon = '🕵'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


render_app_header(scope, page_title, page_icon)

if scope.users['logged_in']:

	ticker = scope.pages[page]['selectors']['ticker']

	if ticker != 'select a ticker' :
		metadata = fetch_yfinance_metadata(ticker)
		# print(metadata)
		if metadata.info != None:
			company_general(metadata)

			# business_summary(metadata)
			fundamental(metadata)
			general(metadata)
			market_info(metadata)

			dividends(metadata)

			print('None of the financial statements are coming out now')
			# financial_statements(metadata)
			# major(metadata)
			# institutional(metadata)
			# annual(metadata)
			# quarterly(metadata)
			# balance_sheet(metadata)
			# balance_sheet_qtr(metadata)
			# cashflow(metadata)
			# cashflow_qtr(metadata)
			# earnings(metadata)
			# earnings_qtr(metadata)
			print('Calendar no longer available')
			# calendar(metadata)
			news(metadata)

			# plot_basic_chart(scope)		
			# view_ticker_file(scope, ticker)
		else:
			st.error('Y Finance did not return any Information')
