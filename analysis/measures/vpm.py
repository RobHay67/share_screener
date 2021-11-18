



def vpm(scope, plot_df, measure):
	# Add a Volume Per Minute (VPM)

	# Not on Investpedia - Rob made this one up specifically for Volume
	
	ticker = scope.selected[scope.display_page]['ticker_list'][0]

	minutes_per_day = scope.ticker_index.loc[ticker]['minutes_per_day']

	plot_df['vpm'] = (plot_df['volume'] / minutes_per_day).astype(int)
