import pandas as pd
import streamlit as st





from ticker.index.update import with_latest_download



def new_tickers_from_web(scope):
	st.info('Downloading Ticker Index information for the ' + scope.share_market)
	if scope.share_market == 'ASX':
		url = 'https://asx.api.markitdigital.com/asx-research/1.0/companies/directory/file?'
		column_names = ['share_code', 'company_name', 'listing_date', 'industry_group', 'market_cap' ]
		downloaded_ticker_info = pd.read_csv( 	url, 
												skiprows=1, 
												names=column_names, 
												header=0, 
												dtype={
													'share_code':'str',
													'company_name':'str',
													'industry_group':'str',
													'market_cap':'float',
												},
												parse_dates=['listing_date'])
		downloaded_ticker_info['share_code'] = downloaded_ticker_info['share_code'] + '.AX'
		downloaded_ticker_info['listing_date'] = pd.to_datetime( downloaded_ticker_info['listing_date'].dt.date  )

		# format the industry group field - remove redundant values
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].fillna('zz_industry_group')
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.replace(', ', '_' )
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.replace(' ', '_' )
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.replace('&', 'and' )
		downloaded_ticker_info['industry_group'] = downloaded_ticker_info['industry_group'].str.lower()

		st.success('number of downloaded ' + scope.share_market + ' ticker codes = ' + str(len(downloaded_ticker_info)))
		with_latest_download(scope, downloaded_ticker_info )
		scope.dropdown_lists_need_updating = True
	else:
		st.error('DOWNLOAD Ticker data NOT YET CONFIGURED FOR ' + scope.share_market)
		pass





