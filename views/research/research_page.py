import streamlit as st

from views.header.controller import render_app_header
from y_finance.metadata import fetch_yfinance_metadata
from views.research.info import company_general
# from views.research.info import business_summary
from views.research.info import fundamental
from views.research.info import general
from views.research.info import market_info
from views.research.dividends import dividends
from views.research.investors import institutional
from views.research.investors import major
from views.research.financials import financial_statements
from views.research.financials import annual
from views.research.financials import quarterly
from views.research.financials import balance_sheet
from views.research.financials import balance_sheet_qtr
from views.research.financials import cashflow
from views.research.financials import cashflow_qtr
from views.research.financials import earnings
from views.research.financials import earnings_qtr
from views.research.calendar import calendar
from views.research.news import news


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
