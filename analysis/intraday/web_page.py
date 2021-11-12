import streamlit as st



from web_charts import plot_candlestick, plot_line_chart, plot_candlestick_seperate_volume, financial_chart_tutorial
# from indicators import line_sma

from web_components import render_data_loader

from analysis.share_data import extract_ticker

# import analysis.get_share_data
# ==============================================================================================================================================================
# Daily Analysis Render Controller
# ==============================================================================================================================================================

def render_intraday(scope):
	st.header('Intra Day Analysis')
	
	render_data_loader(scope, 'intraday')
	
	st.markdown("""---""")

	ticker = scope.ticker['intraday']


	if ticker in list(scope.share_data_files.keys()):
		# col1,col2 = st.columns([2, 10])
		df_row_limit = None if scope.analysis_apply_limit=='False' else int(scope.analysis_limit_share_data)

		share_data = extract_ticker(scope, ticker, df_row_limit)  # this only gets refreshed if the ticker changes or the no of rows changes

	# 	# TODO - this might be the place to add measures - but only if the have not already been add
	# 	# so - we might collect the measures from the screen.....
	# 	# add the measures to a list and pass the list to a cached function that is responsible
	# 	# 	a) adding any new measures
	# 	# 	b) deleted any removed measures
	# 	# ????? should we record the selected measures if we change screen --- maybe the widgets will keep it 
	# 	# render_alternative_indicators(scope)


	# 	# render_indicator_selectors(scope)
		
	# 	# Financial Chart adds the following
	# 	# Index(['date', 'open', 'high', 'low', 'close', 'volume', 'MA20', 'MA5'], dtype='object')

	# 	# financial_chart_tutorial(share_data)

	# 	plot_candlestick_seperate_volume(share_data)

	# 	plot_candlestick(share_data)
		
	# 	plot_line_chart(share_data)