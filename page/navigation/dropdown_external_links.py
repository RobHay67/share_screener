import logging
import streamlit as st
import webbrowser


# Keep this module in the header section as it called by the quicklinks
# module and also the verdicts module

def choose_default_external_link(scope):
	logging.warning('choose_default_external_link')
	page = scope.display['page']
	widget_key = 'widget_' + page + '_button_default_external_link'
	list_external_links = list(scope.config['external_links'].keys())
	
	previous_selection = scope.page[page]['external_link']
	pos_for_previous = list_external_links.index(previous_selection)

	st.selectbox(
				label		='Choose Default URL',
				# label 		='',
				index		=pos_for_previous,
				options		=list_external_links,
				on_change	=clicked_external_url_button,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				),


def clicked_external_url_button(scope, page, widget_key):
	website = scope[widget_key]
	scope.page[page]['external_link'] = website


def button_external_link(scope, ticker):
	logging.critical('button_external_link')
	page = scope.display['page']
	website = scope.page[page]['external_link']
	logging.critical(f"{website=}")
	widget_key = 'widget_' + page + '_button_external_link_' + ticker
	# button_label = website
	st.button(
				label = website, 
				use_container_width=True, 
				on_click=clicked_button_external_url, args=(scope, ticker, widget_key, ),
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





