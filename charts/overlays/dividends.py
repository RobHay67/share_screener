import pandas as pd
import plotly.graph_objects as go

from ticker.model.metadata import fetch_yfinance_metadata


def dividend_cols( scope, chart_df, chart):
	print('adding dividend_cols')
	print(chart)
	page 	= scope.page_to_display
	ticker 	= scope.pages[page]['ticker_list'][0]

	

	# Fetch the Dividend Information for this ticker
	metadata = fetch_yfinance_metadata(ticker)
	dividend_df = pd.DataFrame(metadata.dividends)
	dividend_df.reset_index(inplace=True)
	# dividend_df = dividend_df.rename(columns={'Date': 'date', 'Dividends':chart})

	dividend_dict = dict(zip( dividend_df['Date'], dividend_df[ 'Dividends' ]))		# this creates a dictionary containing the { right joing index : new_column value }		
	chart_df[chart] = chart_df['date'].map( dividend_dict )					# map the new column values to the receiving dataframe
	# chart_df[chart].replace(np.nan, '0', inplace=True)
	# chart_df[chart].fillna(0, inplace=True)

	print(chart_df[chart].head(10))



def dividend_plot(scope, fig, overlay, chart_df, row_no, col_no):
	print('dividend_plot')
	page 	= scope.page_to_display
	ticker 	= scope.pages[page]['ticker_list'][0]

	# ax_candle.scatter( share_df.index, share_df['trade_buy' ],   label = 'Buy',  marker = 'X', color = 'blue' )


	dividend_dict = dict(zip(chart_df['date'], chart_df[overlay]))

	for date, dividend in dividend_dict.items():
		if pd.isna(dividend) == False:
			print('We have a dividend of ', dividend, ' on this date > ', date)
		# print ( date, ' - ', dividend)
		# print(pd.isna(dividend))






	# line_colour = scope.charts[overlay]['plot']['colour']

	# fig.add_trace(go.Scatter(
	# 							mode	= 'markers',
	# 							x		= chart_df['date'], 
	# 							y		= chart_df[overlay],
	# 							opacity	= 0.7, 
	# 							marker_symbol = 4,
	# 							# marker	= {
	# 							# 			'color':'blue', 
											
	# 							# 			'line':{

	# 							# 				width:2,


	# 							# 			}
	# 							# 			# 'marker':'X', 
	# 							# 			}, 


	# 							# label	= 'Dividend',
								
								
	# 							# color   = 'blue',
								 
	# 							name	= overlay
	# 						), 
	# 				row		= row_no, 
	# 				col		= col_no
	# 			)







def ema_cols( scope, chart_df, chart):
	# add an Exponential Moving Average (EMA)
	
	# EMA  = https://www.investopedia.com/terms/e/ema.asp

	column 		= scope.charts[chart]['data_cols']['column']
	no_of_days 	= scope.charts[chart]['data_cols']['periods']

	chart_df[chart] = chart_df[column].ewm(span=no_of_days, adjust=False).mean()



def ema_plot(scope, fig, overlay, chart_df, row_no, col_no):

	line_colour = scope.charts[overlay]['plot']['colour']

	fig.add_trace(go.Scatter(
								x		= chart_df['date'], 
								y		= chart_df[overlay], 
								opacity	= 0.7, 
								line	= {
											'color':line_colour, 
											'width':2
											},  
								name	= overlay
							), 
					row		= row_no, 
					col		= col_no
				)