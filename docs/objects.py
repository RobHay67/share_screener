


# ========================================================================================================================================================================
# Primary Objects
#  description									type					Description
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ticker_index 									DataFrame  				A list of all tickers available to the application
# ticker_data_files								dict of DataFrames		All Share Data files indexed by Ticker Code
# scope.selected[page]['analysis_df'][ticker]	DataFrame				A Specific Ticker Extract from the share_data_files for a particular analysis page
# scope.selected[page]['plot_df]['ticker]		DataFrame				A single Ticker copy of the analysis_df with all the measures added for plotting




#							------------------------------
#							|  scope.ticker_data_files   |				Dictionary of all loaded and downloaded (combined) OHLCV ticker data - this is saved
#							------------------------------




#							---------------------
#							|					|
#							|    analysis_df   	|						Dataframe - copy of Ticker or Tickers being analysed
#							|					|						User defined file size - i.e. latest X rows - limit analysis to 100 rows for faster analysis
#							---------------------						Only refreshes when the ticker_data_file has changed - i.e. we downloaded more data



#							---------------------
#							|					|
#							|      chart_df   	|						Dataframe - copy of analysis_df on which plotting columns are added
#							|					|						i.e. 20 day SMA plot column
#							---------------------



