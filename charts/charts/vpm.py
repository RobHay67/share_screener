



def vpm_cols(scope, chart_df, measure):
	# Add a Volume Per Minute (VPM)

	# Not on Investpedia - Rob made this one up specifically for Volume

	page  	= scope.page_to_display
	
	ticker 	= scope.selected[page]['ticker_list'][0]

	minutes_per_day = scope.ticker_index.loc[ticker]['minutes_per_day']

	chart_df['vpm'] = (chart_df['volume'] / minutes_per_day).astype(int)


def vpm_plot():
	print( 'VPM plot')