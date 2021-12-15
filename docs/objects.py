


# ========================================================================================================================================================================
# Primary Objects
#  description									type					Description
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ticker_index 									DataFrame  				A list of all tickers available to the application
# ticker_data_files								dict of DataFrames		All Share Data files indexed by Ticker Code
# scope.selected[page]['screener_df'][ticker]		DataFrame				Copy of selected ticker(s) from share_data_files with all metrics added for screening
# scope.selected[page]['plot_df]['ticker]		DataFrame				Copy of selected ticker(s) from share_data_files with all metrics added for plotting


#																				-----------------------------
#																				|							|
#			dictionary of all loaded and downloaded OHLCV ticker data			|  scope.ticker_data_files  |	
#																				|							|
#																				-----------------------------
#																							|
#																							|
#							  													  subset ticker_data_files
#																			  /								\
#																			 /								 \
#																			/								  \
#																		   /								   \
#													---------------------										---------------------
#													|					|										|					|
#													|    screener_df   	|										|      chart_df   	|
#													|					|										|					|
#													---------------------										---------------------
#
# Copy Ticker(s)from <ticker_data_files>					yes															yes
# Limit rows to <page_row_limit> 							yes															yes				default = 100	
# Refresh when <ticker_data_file> changes					yes															yes				i.e. we downloaded more data










#										  |
#								  copy screener_df
# 									add metrics
#								          |
#								---------------------						Dataframe - copy of screener_df on which plotting columns are added
#								|					|						i.e. 20 day SMA plot column
#								|      chart_df   	|						REFRESH occurens when :after screener_df changes
#								|					|						a) the screener_df changes
#								---------------------						b) use makes a change to most of the charting parameters (except colour)


