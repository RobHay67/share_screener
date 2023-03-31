import pandas as pd

from ticker_index.update import update_ticker_index
from apps.app_header.layer_selectors import refresh_dropdown_lists
from apps.config.ticker_search import scope_ticker_search


def download_ticker_index_data(scope):

	scope.ticker_index['render']['downloading_asx'] = True

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

		downloaded_df.set_index('share_code', inplace=True)
		downloaded_df['listing_date'] = pd.to_datetime( downloaded_df['listing_date'].dt.date  )

		scope.ticker_index['df_downloaded'] = downloaded_df # Cache the downloaded file
		scope.ticker_index['render']['download_success'] = True


		update_ticker_index(scope)

		refresh_dropdown_lists(scope)

		scope_ticker_search(scope)	# refresh the default ticker search list

	else:
		scope.ticker_index['render']['download_market_n_a'] = True
		pass





