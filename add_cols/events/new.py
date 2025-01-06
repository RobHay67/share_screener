


def new_ticker_data_event(scope, ticker):
    # This event is triggered after new ticker data is
	# either loaded or downloaded. 
	#  
	# Set REPLACE_DF status to TRUE
	# For the Chart and Screen Pages
	# 	- set the appropriate CONFIG_GROUP 
	# 	- copy the TEMPLATE_COL_ADDERS 
	# 	-    (replace all columns that are currently active)



	for page in scope.pages['page_list']:

		scope.tickers[ticker][page]['replace_df'] = True

		if page == 'chart':
			scope.tickers[ticker][page]['config_group'] = 'charts'
			scope.tickers[ticker][page]['replace_column'] = scope.charts['template_col_adders'].copy()

		if page == 'screener':
			scope.tickers[ticker][page]['config_group'] = 'trials'
			scope.tickers[ticker][page]['replace_column'] = scope.trials['template_col_adders'].copy()


