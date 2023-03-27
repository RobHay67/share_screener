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
		leader = 'https://trading.anzshareinvesting.com.au/Market/Charts.aspx?asxcode='
		url = leader + ticker_code

	if website == 'asx':
		leader = 'https://www2.asx.com.au/markets/company/'
		url = leader + ticker_code

	if website == 'google':
		leader = 'https://www.google.com/finance/quote/'
		url = leader + ticker_code + ':' + share_market

	if website == 'yahoo':
		leader = 'https://au.finance.yahoo.com/quote/' 
		query = '?p='
		suffix = '&.tsrc=fin-srch'
		url = 	leader + ticker + query + ticker + suffix

	if website == 'market index':
		leader = 'https://www.marketindex.com.au/asx/'
		url = leader + ticker_code.lower()

	if website == 'hot copper':
		leader = 'https://hotcopper.com.au/asx/'
		url = leader + ticker_code.lower()

	if website == 'market watch':
		leader = 'https://www.marketwatch.com/investing/stock/'
		suffix = '/charts?countrycode=au'
		url = leader + ticker_code.lower() + suffix


	url_string = "[" + website + "](" +  url + ")"

	st.write(url_string)


# Url Examples

# https://www.marketindex.com.au/asx/cba
# https://www.google.com/finance/quote/GMA:ASX
# https://au.finance.yahoo.com/quote/CBA.AX?p=CBA.AX&.tsrc=fin-srch
# https://au.investing.com/equities/commonwealth-bank-of-australia
# https://trading.anzshareinvesting.com.au/Market/Charts.aspx?asxcode=CBA
# https://hotcopper.com.au/asx/cba/
# https://www.marketwatch.com/investing/stock/CBA/charts?countrycode=au

