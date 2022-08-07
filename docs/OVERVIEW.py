
# ========================================================================================================================================================================
# Core Application Processes
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 	Initial Application load of the app performs the following processes :

# 		a) Establishment of Scope object
# 		b) Rendering the initial web app structure (based on the scope)
# 		c) Loading the exisiting (or creating an empty if none exists) Ticker Index
#		d) Load the User Configurable Settings

# 	This results in the application rendering the basic application structure in a web browser

# 	The user then selections an option from the various type of Analysis as follows :
#		
# 		Single Share Ticker Analysis or research on :
# 			(1) Single Ticker (EOD)		> End Of Day (EOD) data		= Charts
#			(2) Single Ticker (ID)  	> Intra Day  (ID ) data		= Charts
# 			(3) Volume Prediction (EOD)	> End Of Day (EOD) data		= Table detailing the predicted volume
# 			(4) Company Research									= Information about the ticker
#
# 		Multiple Ticker Screening - find tickers that meet criteria:
#			(5) Multiple Tickers 		> End Of Day (EOD) data		= Table of tickers meeting configured criteria
#					select from the following :
# 						(a) The entire share market
#						(b) An entire industry within the share market
# 						(c) A Specific Ticker or Tickers
# 					Note : most detailed takes precedence - ie if an industry is selected, this will be used if a market is also selected
# 		
# 
#
#	Loading Data
# 		After selecting an option from the above the application will AUTOMATICALY Load any existing share data
#	
# 	Downloding Data	
# 		The user can supplement any loaded data by choosing to dowload additional data which is AUTOMATICALLY
#		appeneded to any existing data and saved for future analysis
#
#
#	Ticker Data is stored in 			< scope.tickers >
# 	Ticker Screener Data is stored in 	< scope.apps[app].screener_df >		ie scope.apps['single'].screener_df
#	Chart Data is stored in 			< scope.apps[app].chart_df > 			ie scope.apps['single'].chart_df


# Ticker files to be in descending order so that we keep the latest data at the top of the app

