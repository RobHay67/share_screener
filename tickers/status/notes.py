


# -------------------------------------------
# Helpers
# -------------------------------------------

# def replace_cols_status(scope, app, ticker, col_adder_list, col_adder):
	
# 	status = None
# 	# we know the ticker is in the replace_cols ticker_list, 
# 	# we dont know if the col_adder is in the 
# 	# ticker dictionary or whats its status currently is
# 	print( app, ticker, col_adder)
# 	print(col_adder_list)

# 	print(scope.apps[app]['replace_cols'])

# 	if col_adder in col_adder_list: 
# 		# return the status for this col_adder
# 		status = scope.apps[app]['replace_cols'][ticker][col_adder]
# 	else:
# 		# add a column adder for this ticker
# 		scope.apps[app]['replace_cols'][ticker] = [col_adder]
# 		# add set the default status
# 		scope.apps[app]['replace_cols'][ticker][col_adder] = True

# 	return status






Data_frame = 'DataFrame'

# Status
replace_columns = True

print('Rob we are working on the new structure for the scope.tickers')


# so we have a app ticker list 

scope_data = {
	'tickers':	{
					'CBA':	{
								'df':Data_frame,
								'replace_app_dfs':True, 		# True or False - if True, we replace all of the columns anyway
								# 'replace_columns':True,			# this could serve as a shortcut to save iterating through all the app config
								# pages/apps
								'apps': {
											'single':	{
															'df':Data_frame,
															# 'replace_app_dfs':True, 		# Not needed - do at header only
															'candlestick':replace_columns,
															'macd': replace_columns, 
															'macd_vol': replace_columns, 
															'rsi': replace_columns, 
															'vol_osssy': False, 
															'stochastic': replace_columns, 
															'sma_1': replace_columns, 
															'sma_2': False, 
															'sma_3': False, 
															'ema_1': False, 
															'ema_2': False, 
															'ema_3': False, 
															'bollinger_bands': False, 
															'dividends': replace_columns, 
															'candlestick': replace_columns, 
															'scatter': False, 
															'bar': False, 
															'line': replace_columns, 
															'heiken_ashi': False, 
															'volume': replace_columns, 
															'vol_per_minute': False, 
															'vac': False,
															'announcements': False, 
															'ichi_moku': False, 
															'ichi_moku_daily': False
														},
											'screener':	{
															'df':Data_frame,
															# 'replace_app_dfs':True, 		# Not needed - do at header only
															'trend_open': False, 
															'trend_high': replace_columns, 
															'trend_low': False, 
															'trend_close': replace_columns, 
															'trend_volume': False,
														},
										},
							},
				},
	}


# print(scope.apps['templates']['charts'])


# so when we load a file - we just add the appropriate app config from the defaults. The true will signifiy that the 
# columns need replacing. After replacing, set the status to false to prevent further updates




# Events that require the dataframe or the app columns to be replaced or recalculated
#		Transaction							which ticker(s)				app dataframes		app dataframe columns				function to set status
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# a)	Load A ticker data file				1 Ticker					xReplace All Dfs 	Replace ALL Columns
# b)	Change the < page_row_limit >		EVERY Ticker				xReplace All Dfs 	Replace ALL Columns
# c)	Activate an chart/overlay/trial		Every Ticker Using object	ignore				Replace cols for this object
# d)	Deactive a chart/overlay/trial		ignore						ignore				ignore
# g)	Change Value in chart/overlay/trial	Every Ticker Using object	ignore				Replace cols for this object


# x) 	ticker added to app ticker list		we need to add the column adders for this app



# Current app and usage of column adders
# APP		Objects
# --------------------------------------------
# single	charts and overlays
# intraday	none
# volume	none
# research	none
# screener	trials



# so a change to the trials or charts requires all trials to be updated
# but we only update the columns when we are rendering for that stock




# The Current Functions
# set_replace_df_status_for_ticker_and_page
# set_replace_col_adder_status_for_ticker_and_page		replace.py > replace_cols

# set_replace_df_status_for_ticker						load.py combiner.py
# set_replace_col_status_for_ticker						load.py combiner.py

# x set_replace_df_status_for_all_tickers				row_limit.py
# set_replace_cols_status_for_all_tickers				no calls
# 
# set_replace_col_status_for_col_adder					active > on_change_active_status (charts and trials), number, ohlc, ohlcv, trend  (trials??)

# replace_dfs											set_replace_df_status_for_ticker_and_page, set_replace_df_status_for_ticker
# replace_cols


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Load ticker for cba						T-r_df	T-r_dfl ------			------			-------		-------			-------		= refresh the tickers that have changed
#											T-r_col	T-r_col ------			------			-------		-------			-------
# Download new ticker for cba + NAB			T-r_df	T-r_dfl ------			-------			T-r_df		T-r_df			-------		= refresh the tickers that have changed
#											T-r_col	T-r_col ------			------			-------		-------			-------
# Change the < page_row_limit >				T-r_all T-r_all T-r_all			T-r_all			T-r_all		T-r_all			T-r_all		= refresh all tickers and rerun all active add_cols
# Activate overlay or 2nd chart				------	------	------			T-r_col			T-r_col		T-r_col			T-r_col		= recalculate the specific add_cols only	for NON screener pages							
# Update value in overlay or 2nd chart		------	------	------			T-r_col			T-r_col		T-r_col			T-r_col		= recalculate the specific add_cols only	for NON screener pages	
# Activate a col_adder						T-r_col	T-r_col	T-r_col			-------			-------		-------			-------		= recalculate the specific add_cols only	for screener app
# Change col_adder value 					T-r_col	T-r_col	T-r_col			-------			-------		-------			-------		= recalculate the specific add_cols only	for screener app
# Replace the page_df on single app		R-r_df	-------	-------			-------			-------		-------			-------
# Rerun the column adder single app		R-r_col	-------	-------			-------			-------		-------			-------		


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# KEY		Description				Pages		Tickers		Dataframe									add_columns	replace_cols							Replace DF Func		Replace Cols Func		
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# T-r_df 	tag to replace df		All			Specific	set_replace_df_status_for_ticker			------------------------------------------------	replace_dfs			---------------------	
# T-r_col	tag to add_cols			All			Specific	-----------------------------------------	set_replace_col_status_for_ticker					--------------- 	replace_cols
# t-col		change col_adder		All			All			-----------------------------------------	set_replace_col_status_for_col_adder					---------------		replace_cols
# t-ALL 	replace all dfs	& cols	All			All			set_replace_df_status_for_all_tickers 		set_replace_cols_status_for_all_tickers 				replace_dfs			replace_cols
# Rdf		replace the DF			Specific	Specific	set_replace_df_status_for_ticker_and_page	------------------------------------------------	
# Rcol		replace the cols		Specific	Specific	-----------------------------------------	set_replace_col_adder_status_for_ticker_and_page





