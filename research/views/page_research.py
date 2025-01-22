import streamlit as st

from app.views.header.controller import show_page_header
from tickers.model.y_finance.meta_data.metadata import fetch_yfinance_metadata

from research.views.info import company_general
# from research.views.info import business_summary
from research.views.info import fundamental
from research.views.info import general
from research.views.info import market_info
from research.views.dividends import dividends
from research.views.investors import institutional
from research.views.investors import major
from research.views.financials import financial_statements
from research.views.financials import annual
from research.views.financials import quarterly
from research.views.financials import balance_sheet
from research.views.financials import balance_sheet_qtr
from research.views.financials import cashflow
from research.views.financials import cashflow_qtr
from research.views.financials import earnings
from research.views.financials import earnings_qtr
from research.views.calendar import calendar
from research.views.news import news


# TODO - I like this example from the ASX for CBA - https://www2.asx.com.au/markets/company/cba

# Page Configuration
scope = st.session_state
scope.config['display'] = 'research'


show_page_header(scope)

if scope.users['logged_in']:

	ticker = scope.page[page]['selectors']['ticker']

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
