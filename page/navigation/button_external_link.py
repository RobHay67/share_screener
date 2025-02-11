import logging
import streamlit as st
import webbrowser


def button_external_link(scope, ticker):
	logging.debug('button_external_link')
	page = scope.display['page']
	website = scope.page[page]['external_link']
	widget_key = 'widget_' + page + '_button_external_link_' + ticker
	
	st.button(
				label = website, 
				use_container_width=True, 
				on_click=clicked_button_external_url, 
				args=(scope, ticker, widget_key, ),
				key			=widget_key,
				
				)


def clicked_button_external_url(scope, ticker, widget_key):
	logging.warning('clicked_open_external_url')
	page = scope.display['page']
	share_market = scope.config['share_market']
	market_code = scope.config['markets'][share_market]['ticker_suffix']
	website = scope.page[page]['external_link']
	# Remove the market suffix from the share code
	ticker_code = ticker.removesuffix(market_code)

	leader = scope.config['external_links'][website]['leader']
	query = scope.config['external_links'][website]['query']
	suffix = scope.config['external_links'][website]['suffix']

	match website:
		case 'eTrade'		:url = leader + ticker_code
		case 'asx'			:url = leader + ticker_code
		case 'google'		:url = leader + ticker_code + ':' + share_market			
		case 'yahoo'		:url = 	leader + ticker + query + ticker + suffix			
		case 'market index'	:url = leader + ticker_code.lower()
		case 'hot copper'	:url = leader + ticker_code.lower()
		case 'market watch'	:url = leader + ticker_code.lower() + suffix
		case '_'			:'www.theage.com.au'
			
	webbrowser.open(url)

