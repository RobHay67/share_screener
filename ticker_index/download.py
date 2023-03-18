import pandas as pd

from ticker_index.update import update_index
from apps.app_header.dropdowns import refresh_dropdown_lists
from apps.messages.ticker_index import message_download_ticker_index_asx
from apps.messages.ticker_index import message_index_download_success
from apps.messages.ticker_index import message_index_not_asx

# from apps.

def download_ticker_index_data(scope):
	message_download_ticker_index_asx(scope)

	if scope.config['share_market'] == 'ASX':
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

		message_index_download_success(scope, downloaded_ticker_info)

		update_index(scope, downloaded_ticker_info )

		refresh_dropdown_lists(scope)

	else:
		message_index_not_asx(scope)
		pass





