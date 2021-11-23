import streamlit as st

from ticker.downloader.y_finance import fetch_yfinance_metadata
from analysis.views.research.company_general import company_general
from analysis.views.research.dividends import dividends
from analysis.views.research.fundamental import fundamental
from analysis.views.research.general import general
from analysis.views.research.market_info import market_info



# TODO - I like this example from the ASX for CBA - https://www2.asx.com.au/markets/company/cba




# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Company Research Page Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_research_page(ticker):
	
	meta_data, info, divs = fetch_yfinance_metadata(ticker)

	company_general(info)
	dividends(divs)
	fundamental(info)
	general(info)
	# plot_basic_chart(scope)		
	market_info(info)
	# view_ticker_file(scope, ticker)













