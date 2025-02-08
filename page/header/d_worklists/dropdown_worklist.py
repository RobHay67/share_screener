import logging
import streamlit as st

def dropdown_worklist(scope):
	logging.debug("dropdown_worklist")
	page = scope.display['page']
	
	worklist = scope.page[page]['list_page_worklist']
	widget_key = 'widget_' + page + '_list_page_worklist'
	
	# widget_label
	widget_label = 'Unknown Label'	
	no_of_tickers = len(worklist)-1 # as a default is inserted at the top
	if no_of_tickers  < 1:widget_label = 'Worklist (0 Loaded Tickers - Empty)'
	if no_of_tickers == 1:widget_label = 'Worklist (1 Loaded Ticker)'
	if no_of_tickers  > 1:widget_label = 'Worklist (' + str(no_of_tickers) + ') Loaded Tickers'

	previous_selection = scope.page[page]['show']['ticker_file']
	pos_for_previous = worklist.index(previous_selection)	

	selectbox = st.selectbox(
			label		=widget_label, 
			options		=worklist,
			index		=pos_for_previous, 
			on_change	=changed_worklist_item_to_display,
			args		=(scope, page, widget_key ),
			key			=widget_key,
			)

	return selectbox


def changed_worklist_item_to_display(scope, page, widget_key):
	logging.warning("changed_worklist_item_to_display")
	selected_ticker = scope[widget_key]
	# store the selection
	scope.page[page]['show']['ticker_file'] = selected_ticker	


