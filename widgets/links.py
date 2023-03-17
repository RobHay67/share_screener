import streamlit as st
# import webbrowser


# def hyperlink_to_app_link(scope, new_app_page, ticker):





def link_to_app_button(scope, app, ticker):

	widget_key = app + '_' + ticker + '_button'
	if app == 'chart':
		app_desc = '📊'
	elif app == 'volume':
		app_desc = '🔊 '
	elif app == 'intraday':
		app_desc = '🌤️'
	elif app == 'research':
		app_desc = '🕵'
	else:
		app_desc = app


	st.button(
				# label=app.title(), 
				label=app_desc,
				key=widget_key,
				use_container_width=True,
				on_click=open_app,
				args=(scope, app, ticker)
				)

def open_app(scope, app, ticker):
	
	scope.apps['display_app'] = app

	if app != 'screener':	
		scope.apps[app]['selectors']['ticker'] = ticker
	else:
		scope.apps[app]['selectors']['tickers'] = [ticker]
		scope.apps[app]['selectors']['industries'] = []
		scope.apps[app]['selectors']['market'] = 'select market'
		scope.apps[app]['search_results'] = {}


def website_hyperlink(scope, website, ticker):

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

	if website == 'market index':
		url = 'https://www.marketindex.com.au/asx/'
		external_url = url + ticker_code.lower()

	if website == 'hot copper':
		url = 'https://hotcopper.com.au/asx/'
		external_url = url + ticker_code.lower()


	url_string = "[" + website + "](" +  external_url + ")"

	st.write(url_string)


# Url Examples

# https://www.marketindex.com.au/asx/cba
# https://www.google.com/finance/quote/GMA:ASX
# https://au.finance.yahoo.com/quote/CBA.AX?p=CBA.AX&.tsrc=fin-srch
# https://au.investing.com/equities/commonwealth-bank-of-australia
# https://trading.anzshareinvesting.com.au/Market/Charts.aspx?asxcode=CBA
# https://hotcopper.com.au/asx/cba/

