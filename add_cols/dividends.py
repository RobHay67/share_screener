import pandas as pd


from data.tickers.metadata import fetch_yfinance_metadata


def dividend_cols( scope, chart, ticker, chart_df):

	page 	= scope.pages['display_page']
	# ticker 	= scope.pages[page]['ticker_list'][0]

	# Fetch the Dividend Information for this ticker
	metadata = fetch_yfinance_metadata(ticker)
	dividend_df = pd.DataFrame(metadata.dividends)
	dividend_df.reset_index(inplace=True)
	# dividend_df = dividend_df.rename(columns={'Date': 'date', 'Dividends':chart})
	dividend_df['Date'] = pd.to_datetime( dividend_df['Date'].dt.date  )

	dividend_dict = dict(zip( dividend_df['Date'], dividend_df[ 'Dividends' ]))		# this creates a dictionary containing the { right joing index : new_column value }		
	chart_df[chart] = chart_df['date'].map( dividend_dict )							# map the new column values to the receiving dataframe



