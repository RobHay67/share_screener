


# ========================================================================================================================================================================
# Primary Objects
#  description									type					Description
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ticker_index 									DataFrame  				A list of all tickers available to the application
# ticker_data_files								dict of DataFrames		All Share Data files indexed by Ticker Code
# scope.selected[page]['df'][ticker]			DataFrame				Copy of selected ticker(s) from share_data_files with all add_cols added for screening
# scope.selected[page]['df]['ticker]			DataFrame				Copy of selected ticker(s) from share_data_files with all add_cols added for plotting


#																		---------------------------------
#																		|								|
#	dictionary of all loaded and downloaded OHLCV ticker data			|   scope.data['ticker_files']  |	
#																		|								|
#																		---------------------------------
#																					|
#																					|
#							  										copy specific <ticker_data_files> only
# 														specific tickers stored in < scope.pages[page]['ticker_list] >
# 																Limit rows to < page_row_limit > default = 100	
#																   /				|				 \
#															  	  /					|			 	  \
#																 /					|			  	   \
#																/					|			   		\
#											---------------------			---------------------		---------------------
#											| 	 scope.pages	|			| 	 scope.pages	|		| 	 scope.pages	|
# 											|	 ['screener']	|			|	  ['single']	|		|	['intra_day']	|
#											|    	[df]   		|			|     	[df]   		|		|      [df]   		|
#											|					|			|					|		|					|
#											---------------------			---------------------		---------------------
#
# example (page.ticker_list)				[cba 	NAB		anz ]			[ifl			NAB ]		[NAB			wbc ]
#
#
# Events that change the data
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ? Load ticker for cba						DF+Cols	------	------			------			------		------			------		= refresh the tickers that have changed
# ? Download new ticker for cba + NAB		DF+Cols	DF+Cols	------			------			DF+Cols		DF+Cols			------		= refresh the tickers that have changed
# ? Change the < page_row_limit >			Both---	Both---	Both---			Both---			Both---		Both---			Both---		= refresh all tickers and rerun all active add_cols
# ? Activate overlay or 2nd chart			------	------	------			Cols			Cols		Cols			Cols		= recalculate the specific add_cols only	for NON screener pages							
# ? Update value in overlay or 2nd chart	------	------	------			Cols			Cols		Cols			Cols		= recalculate the specific add_cols only	for NON screener pages	
# ? Activate a col_adder					Cols		Cols		Cols	------			------		------			------		= recalculate the specific add_cols only	for screener page
# ? Change col_adder value 					Cols		Cols		Cols	------			------		------			------		= recalculate the specific add_cols only	for screener page

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# KEY	Description				Tickers		add_cols	Page(s)	DF Status Function 		add_cols status Func		Update DFS Func	add_cols Func			Copy From					Changes / Updates				
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# DF 	replace df & add_cols	Specific	Every		Every	set_replace_df_status	set_rerun_col_adder_status 	replace_dfs		various					scope.data['ticker_files']	scope.pages[page]['dfs'][ticker]	
# Cols	add_cols				Every		Specific	Every	set_replace_df_status	set_rerun_col_adder_status 	replace_dfs		various					-------------------------	scope.pages[page]['dfs'][ticker]
# Both 	replace df & add_cols	Every		Every		Every	set_replace_df_status	set_rerun_col_adder_status 	replace_dfs		various					scope.data['ticker_files']	scope.pages[page]['dfs'][ticker]	
# -----  Not Required ------	Specific	Specific	This combination only happens when we have a single ticker and will be covered by the other options anyway
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

# Rs 	= Copy and Replace changed 	ticker DF  from < scope.data.ticker_files >				???? - Function Added
# CaM 	= re Calculate ALL     		active add_cols for every Ticker in the page			???? - Function Added
# Cols	= re Calculate changed 		active add_cols for every Ticker in the page 			???? - Function Added

# tag the add_cols when they have been run													???? - updated function
# update the scope.page_metrics after changes made 											????
# change the test after editing scope.page_metrics											????
# change the chart  after editing scope.page_metrics										????


