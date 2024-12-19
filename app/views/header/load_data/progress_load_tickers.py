import streamlit as st


from tickers.load.controller import load_ticker


def progress_bar_loading_tickers(scope):
	
	progress_bar_exists = False
	list_of_tickers_to_load = create_ticker_list_to_load(scope)

	if len(list_of_tickers_to_load) > 0:
		
		no_of_tickers = len(list_of_tickers_to_load)

		if progress_bar_exists==False:
			my_bar = st.progress(0)
			progress_bar_exists = True

		for counter, ticker in enumerate(list_of_tickers_to_load):
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Loading ohlcv Ticker File ( '+str(counter)+' )  > '+ticker)
			load_ticker(scope, ticker)
	
	# we will have new information after the load so update
	# the dropdown list for the worklist
	build_app_worklist_dropdown(scope)

	no_loaded_tickers = str(len(scope.tickers.keys()))

	if progress_bar_exists==True:
		my_bar.progress(100, text='All files loaded ( '+no_loaded_tickers+' )')
	else:
		
		my_bar = st.progress(100, text='Already Loaded ( '+no_loaded_tickers+ ' ) tickers. No additional Files to Load')