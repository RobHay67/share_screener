
# ========================================================================================================================================================================
# Branch Strategy
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                          -      Main  (picked up by Streamlit)	_
#						/					|							\
#					/						|							  \	
#          release_01					release_02						release_03
#				|						 /		   \						|		\
#				|						/			\						|		 \
#		add_sidebar   				load_data	save_data				add_charts   all_market_strategy
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# general idea we can more easily role back to a release branch (hopefully) and see the flow of the branch into the release


# Primary Objects
# Ticker Index 			DataFrame  				A list of all tickers available to the application
# share_data_files		dict of DataFrames		All Share Data files indexed by Ticker Code





# ========================================================================================================================================================================
# Core Application Processes
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 	Initial Application load of the app performs the following processes :

# 		a) Establishment of Scope object
# 		b) Rendering the initial web page structure (based on the scope)
# 		c) Loading the exisiting (or creating an empty if none exists) Ticker Index

# 	This results in the application rendering the basic application structure in a web browser

# 	The user then decides between the various options including :
# 		Multiple Share Ticker Analysis on either:
# 				a) The entire share market
#				b) An entire industry within the share market
# 				c) A Specific Ticker or Tickers
# 		Single Share Ticker Analysis or research on :
# 				b) End Of Day (EOD) analysis
#				c) Intra Day  (ED)  analysis
# 				e) End Of Day (EOD) prediction of volume
# 				d) Researching a Company
# 
# 	Process after selecting the appropriate option
#				1) Select a ticker or group of tickers (selections are independent for each option)
#				2) Load existing share data
#				3) Download share data (and append to any existing date - auto saved for next time)
#
#	Application processing
#				a) copy selected ticker(s) share data from the share_data_files dictionary
#				b) 
#
#				ok - now it gets tough
#				do we add the measures before trying to render the charts????
#
#
#


