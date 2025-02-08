import logging
import streamlit as st





def website_hyperlink(scope, website, ticker):
	logging.warning("website_hyperlink")
	pos = ticker.find(".")
	ticker_code = ticker[0:pos]
	share_market = scope.config["share_market"]

	match website:
		case "eTrade":
			leader = "https://trading.anzshareinvesting.com.au/Market/Charts.aspx?asxcode="
			url = leader + ticker_code
		case "asx":
			leader = "https://www2.asx.com.au/markets/company/"
			url = leader + ticker_code
		case "google":
			leader = "https://www.google.com/finance/quote/"
			url = leader + ticker_code + ":" + share_market
		case "yahoo":
			leader = "https://au.finance.yahoo.com/quote/" 
			query = "?p="
			suffix = "&.tsrc=fin-srch"
			url = 	leader + ticker + query + ticker + suffix
		case "market index":
			leader = "https://www.marketindex.com.au/asx/"
			url = leader + ticker_code.lower()
		case "hot copper":
			leader = "https://hotcopper.com.au/asx/"
			url = leader + ticker_code.lower()
		case "market watch":
			leader = "https://www.marketwatch.com/investing/stock/"
			suffix = "/charts?countrycode=au"
			url = leader + ticker_code.lower() + suffix

	url_string = "[" + website + "](" +  url + ")"

	website = website.capitalize()
	# st.page_link("http://www.google.com", label="Google", icon="🌎")
	st.page_link(page=url, label=website, icon="🌎")

	# if website == "eTrade":
	# if website == "asx":
	# if website == "google":
	# if website == "yahoo":
	# if website == "market index":
	# if website == "hot copper":
	# if website == "market watch":


	# st.write(url_string)

# [market watch](https://www.marketwatch.com/investing/stock/wbc/charts?countrycode=au)
# Url Examples

# https://www.marketindex.com.au/asx/cba
# https://www.google.com/finance/quote/GMA:ASX
# https://au.finance.yahoo.com/quote/CBA.AX?p=CBA.AX&.tsrc=fin-srch
# https://au.investing.com/equities/commonwealth-bank-of-australia
# https://trading.anzshareinvesting.com.au/Market/Charts.aspx?asxcode=CBA
# https://hotcopper.com.au/asx/cba/
# https://www.marketwatch.com/investing/stock/CBA/charts?countrycode=au

