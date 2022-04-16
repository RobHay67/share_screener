


def vpm_cols( scope, chart, ticker, chart_df):
	# Add a Volume Per Minute (VPM)

	# Not on Investpedia - Rob made this one up specifically for Volume

	page  	= scope.pages['display_page']
	
	# ticker 	= scope.selected[page]['ticker_list'][0]

	minutes_per_day = scope.data['ticker_index'].loc[ticker]['minutes_per_day']

	chart_df['vpm'] = (chart_df['volume'] / minutes_per_day).astype(int)


