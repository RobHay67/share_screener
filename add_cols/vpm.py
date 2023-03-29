


def vpm_cols( scope, chart, ticker, chart_df):
	# Add a Volume Per Minute (VPM)

	# Not on Investpedia - Rob made this one up specifically for Volume

	app  	= scope.apps['display_app']
	
	minutes_per_day = scope.ticker_index['df'].loc[ticker]['minutes_per_day']

	chart_df['vpm'] = (chart_df['volume'] / minutes_per_day).astype(int)


