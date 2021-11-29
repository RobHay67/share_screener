
from picker.controller import ticker_picker
from ticker.model.metadata import fetch_yfinance_metadata

from analysis.view.titles import analysis_titles

from analysis.view.research.info import company_general
from analysis.view.research.info import business_summary
from analysis.view.research.info import fundamental
from analysis.view.research.info import general
from analysis.view.research.info import market_info

from analysis.view.research.dividends import dividends

from analysis.view.research.investors import institutional
from analysis.view.research.investors import major

from analysis.view.research.financials import annual
from analysis.view.research.financials import quarterly
from analysis.view.research.financials import balance_sheet
from analysis.view.research.financials import balance_sheet_qtr

from analysis.view.research.financials import cashflow
from analysis.view.research.financials import cashflow_qtr


from analysis.view.research.financials import earnings
from analysis.view.research.financials import earnings_qtr

from analysis.view.research.calendar import calendar
from analysis.view.research.news import news



# TODO - I like this example from the ASX for CBA - https://www2.asx.com.au/markets/company/cba



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Company Research
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def analysis_research_page(scope):
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












