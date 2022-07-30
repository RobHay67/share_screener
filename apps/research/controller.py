
from apps.ticker_loader.header import render_page_title
from apps.ticker_loader.controller import render_ticker_loader


from data.tickers.metadata import fetch_yfinance_metadata

from apps.research.view.info import company_general
# from apps.research.view.info import business_summary
from apps.research.view.info import fundamental
from apps.research.view.info import general
from apps.research.view.info import market_info

from apps.research.view.dividends import dividends

from apps.research.view.investors import institutional
from apps.research.view.investors import major


from apps.research.view.financials import financial_statements
from apps.research.view.financials import annual
from apps.research.view.financials import quarterly
from apps.research.view.financials import balance_sheet
from apps.research.view.financials import balance_sheet_qtr

from apps.research.view.financials import cashflow
from apps.research.view.financials import cashflow_qtr


from apps.research.view.financials import earnings
from apps.research.view.financials import earnings_qtr

from apps.research.view.calendar import calendar
from apps.research.view.news import news

from apps.ticker_loader.search_results import render_search_results

# TODO - I like this example from the ASX for CBA - https://www2.asx.com.au/markets/company/cba



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Company Research
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_research_page(scope):
	# render_page_title(scope, 'Company Research', 'research')
	render_page_title(scope, 'Company Research')

	render_ticker_loader(scope)
	
	ticker = scope.pages['research']['selectors']['ticker']

	if ticker != 'select a ticker' :
		metadata = fetch_yfinance_metadata(ticker)


		company_general(metadata)

		import yfinance as yf
		metadata = yf.Ticker('CBA.AX')
		print(metadata.info)



		
		# business_summary(metadata)
		fundamental(metadata)
		general(metadata)
		market_info(metadata)

		dividends(metadata)


		financial_statements(metadata)


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

	else:
		render_search_results(scope)











