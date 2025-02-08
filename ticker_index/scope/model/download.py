import logging
import pandas as pd

from ticker_index.scope.model.update import update_ticker_index
from config.scope.model.scope_config import scope_dropdown_lists
from config.scope.model.scope_config import scope_ticker_search

from ticker_index.scope.views.download.messages import message_downloading
from ticker_index.scope.views.download.messages import message_completed_download
from ticker_index.scope.views.download.messages import message_failed_market


def download_ticker_index_data(scope):
	logging.warning("download_ticker_index_data")
	if scope.config['share_market'] == 'ASX':
		message_downloading(scope)

		url = 'https://asx.api.markitdigital.com/asx-research/1.0/companies/directory/file?'
		column_names = ['share_code', 'company_name', 'industry_group', 'listing_date', 'market_cap' ]

		downloaded_df = pd.read_csv( 	url, 
										skiprows=1, 
										names=column_names, 
										header=0, 
										dtype={
											'share_code':'str',
											'company_name':'str',
											'industry_group':'str',
											'market_cap':'str',
										},
										parse_dates=['listing_date'])
		
		# TAG Market Information
		downloaded_df['share_code'] = downloaded_df['share_code'] + '.AX'
		
		# format the listing_date
		downloaded_df['listing_date'] = pd.to_datetime( downloaded_df['listing_date'].dt.date)

		# format the industry group field - remove redundant values
		downloaded_df['industry_group'] = downloaded_df['industry_group'].fillna('zz_industry_group')
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.replace(', ', '_' )
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.replace(' ', '_' )
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.replace('&', 'and' )
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.lower()

		# format the market cap ready for transformation into a float
		downloaded_df['market_cap'] = downloaded_df['market_cap'].replace('SUSPENDED', '0')
		downloaded_df['market_cap'] = downloaded_df['market_cap'].replace('--', '0')

		# format the listing date
		downloaded_df.set_index('share_code', inplace=True)
		downloaded_df['listing_date'] = pd.to_datetime( downloaded_df['listing_date'].dt.date  )

		# Download Message
		message_completed_download(scope, downloaded_df)

		# Cache the downloaded file
		scope.ticker_index['download_cache']= downloaded_df 
		update_ticker_index(scope)
		scope_dropdown_lists(scope)
		scope_ticker_search(scope)	# refresh the default ticker search list
				
	else:
		message_failed_market(scope)
		pass




