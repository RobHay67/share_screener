


# Scope Notes


# Terminology
# Scope is the name space that stores all the application variables 
# including the state of the app.
#																				---------Naming Conventions------------
#																				---module-------	-----function------
# config 	: variables managed entirely by the application						config_< name >  	show_scope_< name >
# settings 	: variables that can be changed by the user (i.e. show this chart)	settings_< name >	show_scope_< name >



#						----page required-------	---access from page----
# name			type		config		settings 	Scope		Screener	charts	Intra	Volume	Research	Website	Ticker	Logout	Testing
#																					Day									Index
# -------------------------------------------------------------------------------------------------------------------------------------------------
# summary		summary		Yes			x			Yes			x			x		x		x		x			x		x		Yes		x
# files						DONE		x			Yes			x			x		x		x		x			x		x		x		x
# config					DONE		x			Yes			x			x		x		x		x			x		x		x		x
# ticker_index				Yes			x			Yes			x			x		x		x		x			x		Yes		x		x
# users						DONE		x			Yes			x			x		x		x		x			x		x		x		x
# tickers		DATA		Yes			x			Yes			Yes			Yes		Yes		Yes		x			x		x		x		x
# tickers_config			Yes			x			Yes			x			x		x		x		x			x		x		x		x
# yf						Yes			x			Yes			x			x		x		x		x			x		x		x		x
# page						DONE		x			Yes			Yes			Yes		Yes		Yes		Yes			x		x		x		x
# trials (and verdicts)		DONE		Yes			Yes			Yes			x		x		x		x			x		x		x		x
# strategy					DONE		Yes			Yes			Yes			x		x		x		x			x		x		x		x
# charts (and overlays)		DONE		Yes			Yes			x			Yes		x		x		x			x		x		x		x


# NOTES
# Trials - verdicts should be combined
# tickers (Data) tickers_config and yf CAN BE conbined into a single screen
