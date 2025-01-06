import streamlit as st


def worklist_dropdown(scope):

	page = scope.config['display']
	worklist = scope.page[page]['worklist_long_desc']
	widget_key = 'widget_' + page + '_worklist_long_desc'
	widget_label = determine_appropriate_label(worklist)
	previous_selection = scope.page[page]['render']['ticker_file']
	pos_for_previous = scope.page[page]['render']['ticker_file'].index(previous_selection)	

	selectbox = st.selectbox(
			label		=widget_label, 
			options		=worklist,
			index		=pos_for_previous, 
			on_change	=tag_worklist_item_to_display,
			args		=(scope, page, widget_key ),
			key			=widget_key,
			)

	return selectbox


def tag_worklist_item_to_display(scope, page, widget_key):
	selected_ticker = scope[widget_key]
	# store the selection
	scope.page[page]['render']['ticker_file'] = selected_ticker	
	st.write(selected_ticker)


def determine_appropriate_label(worklist):
	no_of_tickers = len(worklist)-1 # as a default is inserted at the top
	widget_label = 'Unknown Label'
	if no_of_tickers  < 1:widget_label = 'Worklist (Empty)'
	if no_of_tickers == 1:widget_label = 'Worklist (1 Ticker)'
	if no_of_tickers  > 1:widget_label = 'Worklist (' + str(no_of_tickers) + ') Tickers'
	return widget_label

