import pandas as pd

from ticker_index.update import update_index
from apps.app_header.layer_selectors import refresh_dropdown_lists
from apps.messages.ticker_index import message_download_ticker_index_asx
from apps.messages.ticker_index import message_index_download_success
from apps.messages.ticker_index import message_index_not_asx
from apps.config.ticker_search import scope_ticker_search



def download_ticker_index_data(scope):
	message_download_ticker_index_asx(scope)

	if scope.config['share_market'] == 'ASX':
		url = 'https://asx.api.markitdigital.com/asx-research/1.0/companies/directory/file?'
		column_names = ['share_code', 'company_name', 'listing_date', 'industry_group', 'market_cap' ]
		downloaded_df = pd.read_csv( 	url, 
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
		downloaded_df['share_code'] = downloaded_df['share_code'] + '.AX'
		downloaded_df['listing_date'] = pd.to_datetime( downloaded_df['listing_date'].dt.date  )

		# format the industry group field - remove redundant values
		downloaded_df['industry_group'] = downloaded_df['industry_group'].fillna('zz_industry_group')
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.replace(', ', '_' )
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.replace(' ', '_' )
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.replace('&', 'and' )
		downloaded_df['industry_group'] = downloaded_df['industry_group'].str.lower()

		message_index_download_success(scope, downloaded_df)

		update_index(scope, downloaded_df )

		refresh_dropdown_lists(scope)

		scope_ticker_search(scope)	# refresh the default ticker search list

	else:
		message_index_not_asx(scope)
		pass





