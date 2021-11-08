





# Application Control

#							ok			this is good			this is good					this makes sense - we just check in here as needed
# ========================================================================================================================================================================
#  type of control			widget		populated_from			selection_stored_in				ticker_list		loaded_/_download_data_stored_in	
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multi Ticker Analysis		multiselect	dropdown_markets		tickers_market									share_data_files[ticker]
# Multi Ticker Analysis		multiselect	dropdown_industries		tickers_industries								share_data_files[ticker]
# Multi Ticker Analysis		multiselect	dropdown_tickers		tickers_selected								share_data_files[ticker]
# Company Profile			selectbox	dropdown_ticker		 	ticker_for_company_profile		ticker_list		share_data_files[ticker]			
# Volume Predictor			selectbox	dropdown_ticker			ticker_for_vol_predict							share_data_files[ticker]
# Daily Analysis			selectbox	dropdown_ticker			ticker_for_daily								share_data_files[ticker]


col1,col2,col3,col4 = st.columns([2,2,2,6])		

Company Profile			Ticker-selector space buttons 