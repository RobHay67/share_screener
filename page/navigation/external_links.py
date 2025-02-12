import logging
import streamlit as st

# Keep this module in the header section as it called by the quicklinks
# module and also the verdicts module

def selectbox_external_link(scope):
	logging.info('selectbox_external_link')
	page = scope.display['page']
	widget_key = 'widget_' + page + '_button_external_link'
	list_external_links = list(scope.config['external_links'].keys())
	
	previous_selection = scope.config['external_link']
	pos_for_previous = list_external_links.index(previous_selection)

	st.selectbox(
				label		='Choose Default URL',
				# label 		='',
				index		=pos_for_previous,
				options		=list_external_links,
				on_change	=clicked_external_url_link,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				label_visibility='collapsed',
				),


def radio_external_links(scope, ticker):
	logging.info('radio_external_links')
	page = scope.display['page']
	widget_key = 'widget_' + page + '_radio_external_link'
	list_external_links = list(scope.config['external_links'].keys())

	previous_selection = scope.config['external_link']
	pos_for_previous = list_external_links.index(previous_selection)


	st.radio(
				label="Set label visibility",
				index=pos_for_previous,
				options=list_external_links,
				on_change	=clicked_external_url_link,
				args		=(scope, page, widget_key, ),
				# disabled=False,
				horizontal=True,
				key=widget_key,
				label_visibility='collapsed',
   			 )


def clicked_external_url_link(scope, page, widget_key):
	logging.warning('clicked_external_url_link')
	website = scope[widget_key]
	scope.config['external_link'] = website

