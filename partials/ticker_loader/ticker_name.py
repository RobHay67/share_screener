import streamlit as st



def render_ticker_name(scope):

	app = scope.apps['display_app']

	if app != 'screener':

		# there should only be 1 ticker in this list
		
		if len(scope.apps[app]['worklist']) == 1:
			
			# Base Data
			ticker = scope.apps[app]['worklist'][0]
			ticker_name = scope.ticker_search[ticker]

			with scope.col1:
				st.write('')
				st.subheader(ticker_name)

			# Check that we have data for this ticker
			if ticker in list(scope.tickers.keys()): 
				
				ticker_df = scope.tickers[ticker]['df']

				# Date Range
				min_date = ticker_df['date'].min()
				max_date = ticker_df['date'].max()
				min_date = str(min_date).split()[0]
				max_date = str(max_date).split()[0]
				
				# Key Values
				close = str(round((ticker_df['close'].values[0]),2))
				volume = format( (ticker_df['volume'].values[0]), ',d')

				close = round((ticker_df['close'].values[0]),2)
				close = "${:.2f}".format(close)

				with scope.col1:

					st.subheader(close + ' ..... ' + volume)
					st.write(min_date + ' << >> ' + max_date)
			


