
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
	scope.apps[app]['selectors']['ticker'] = ticker


def drill_website_button(scope, website, ticker):

	widget_key = website + '_' + ticker + '_button'

	st.button(
				label=website, 
				key=widget_key,
				on_click=open_asx_website,
				args=(scope, website, ticker)
				)


def open_asx_website(scope, website, ticker):

	pos = ticker.find(".")
	ticker_code = ticker[0:pos]
	share_market = scope.config['share_market']

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


	webbrowser.open(external_url)


# https://www.marketindex.com.au/asx/cba
# https://www.google.com/finance/quote/GMA:ASX
# https://au.finance.yahoo.com/quote/CBA.AX?p=CBA.AX&.tsrc=fin-srch
# https://au.investing.com/equities/commonwealth-bank-of-australia