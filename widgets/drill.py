
import streamlit as st
import webbrowser


# This function should only be available from the screener page



def drill_app_button(scope, app, ticker):

	widget_key = app + '_' + ticker + '_button'

	st.button(
				label=app.title(), 
				key=widget_key,
				on_click=drill_app,
				args=(scope, app, ticker)
				)

def drill_app(scope, app, ticker):
	scope.apps['display_app'] = app

	if app != 'screener':	
		scope.apps[app]['selectors']['ticker'] = ticker
	else:
		scope.apps[app]['selectors']['tickers'] = [ticker]
		scope.apps[app]['selectors']['industries'] = []
		scope.apps[app]['selectors']['market'] = 'select entire market'
		scope.apps[app]['search_results'] = {}

def drill_website_button(scope, website, ticker):

	widget_key = website + '_' + ticker + '_button'

	open_asx_website(scope, website, ticker)

	# st.button(
	# 			label=website, 
	# 			key=widget_key,
	# 			on_click=open_asx_website,
	# 			args=(scope, website, ticker)
	# 			)


def open_asx_website(scope, website, ticker):



	pos = ticker.find(".")
	ticker_code = ticker[0:pos]
	share_market = scope.config['share_market']

	if website == 'eTrade':
		etrade_url = 'https://trading.anzshareinvesting.com.au/Market/Charts.aspx?asxcode='
		external_url = etrade_url + ticker_code


	if website == 'asx':
		asx_url = 'https://www2.asx.com.au/markets/company/'
		external_url = asx_url + ticker_code

	if website == 'google':
		google_url = 'https://www.google.com/finance/quote/'
		external_url = google_url + ticker_code + ':' + share_market

	if website == 'yahoo':
		url = 'https://au.finance.yahoo.com/quote/' 
		query = '?p='
		suffix = '&.tsrc=fin-srch'
		external_url = 	url + ticker + query + ticker + suffix

	if website == 'marketindex':
		url = 'https://www.marketindex.com.au/asx/'
		external_url = url + ticker_code.lower()


	# webbrowser.open(external_url)


	# url_string = website + "[link](" +  external_url + ")"

	url_string = "[" + website + "](" +  external_url + ")"

	# st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")

	st.write(url_string)

	# asxlink


# https://www.marketindex.com.au/asx/cba
# https://www.google.com/finance/quote/GMA:ASX
# https://au.finance.yahoo.com/quote/CBA.AX?p=CBA.AX&.tsrc=fin-srch
# https://au.investing.com/equities/commonwealth-bank-of-australia
# https://trading.anzshareinvesting.com.au/Market/Charts.aspx?asxcode=CBA