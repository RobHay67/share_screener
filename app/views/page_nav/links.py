import streamlit as st
from streamlit_extras.switch_page_button import switch_page





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

