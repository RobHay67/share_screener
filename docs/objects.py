


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
# ? Load ticker for cba						rDF+rCl ------	------			------			------		------			------		= refresh the tickers that have changed
# ? Download new ticker for cba + NAB		rDF+rCl rDF+rCl	------			------			rDF+rCl		rDF+rCl			------		= refresh the tickers that have changed
# ? Change the < page_row_limit >			--ALL-- --ALL-- --ALL--			--ALL--			--ALL--		--ALL--			--ALL--		= refresh all tickers and rerun all active add_cols
# ? Activate overlay or 2nd chart			------	------	------			col				col			col				col			= recalculate the specific add_cols only	for NON screener pages							
# ? Update value in overlay or 2nd chart	------	------	------			col				col			col				col			= recalculate the specific add_cols only	for NON screener pages	
# ? Activate a col_adder					col		col		col				------			------		------			------		= recalculate the specific add_cols only	for screener page
# ? Change col_adder value 					col		col		col				------			------		------			------		= recalculate the specific add_cols only	for screener page

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# KEY	Description				Pages	Tickers		Dataframe								add_columns	replace_cols					Replace DF Func		Replace Cols Func		
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
# rDF 	replace df				All		Specific	set_replace_df_status_for_ticker		---------------------------------------		replace_dfs			---------------------	
# rCl	add_cols				All		Specific	-------------------------------------	set_replace_col_adder_status_for_ticker		--------------- 	replace_added_columns
# col	change col_adder		All		All			-------------------------------------	set_replace_col_status_for_col_adder		---------------		replace_added_columns
# ALL 	replace all dfs	& cols	All		All			set_replace_df_status_for_all_tickers 	set_replace_cols_status_for_all_tickers 	replace_dfs			replace_added_columns
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


# Rs 	= Copy and Replace changed 	ticker DF  from < scope.data.ticker_files >				???? - Function Added
# CaM 	= re Calculate ALL     		active add_cols for every Ticker in the page			???? - Function Added
# rCl	= re Calculate changed 		active add_cols for every Ticker in the page 			???? - Function Added

# tag the add_cols when they have been run													???? - updated function
# update the scope.page_metrics after changes made 											????
# change the test after editing scope.page_metrics											????
# change the chart  after editing scope.page_metrics										????


