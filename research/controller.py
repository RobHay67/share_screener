
from picker.controller import ticker_picker
from tickers.model.metadata import fetch_yfinance_metadata

from pages.view.analysis_title import analysis_titles

from research.view.info import company_general
from research.view.info import business_summary
from research.view.info import fundamental
from research.view.info import general
from research.view.info import market_info

from research.view.dividends import dividends

from research.view.investors import institutional
from research.view.investors import major

from research.view.financials import annual
from research.view.financials import quarterly
from research.view.financials import balance_sheet
from research.view.financials import balance_sheet_qtr

from research.view.financials import cashflow
from research.view.financials import cashflow_qtr


from research.view.financials import earnings
from research.view.financials import earnings_qtr

from research.view.calendar import calendar
from research.view.news import news



# TODO - I like this example from the ASX for CBA - https://www2.asx.com.au/markets/company/cba



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Company Research
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_research_page(scope):
	analysis_titles(scope, 'Company Research', 'research')

	
	ticker = scope.pages['research']['ticker_list'][0]

	if ticker != 'select a ticker':	
		metadata = fetch_yfinance_metadata(ticker)

		company_general(metadata)
		business_summary(metadata)
		fundamental(metadata)
		general(metadata)
		market_info(metadata)

		dividends(metadata)
		major(metadata)
		institutional(metadata)
		annual(metadata)
		quarterly(metadata)
		balance_sheet(metadata)
		balance_sheet_qtr(metadata)
		cashflow(metadata)
		cashflow_qtr(metadata)
		earnings(metadata)
		earnings_qtr(metadata)

		calendar(metadata)
		news(metadata)

		# plot_basic_chart(scope)		
		# view_ticker_file(scope, ticker)












