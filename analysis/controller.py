import streamlit as st

from ticker.loaders.single_loader import single_loader
from ticker.loaders.multi_loader import multi_loader

from analysis.volume import volume_prediction
from analysis.research import view_research_page

from charts.model.chart_df import create_chart_df
from charts.controller import view_charts

from analysis.views.multi_analysis import view_multi_criteria

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def single_ticker_analysis(scope):			# TODO - these should be renamed to single_ticker_analysis
	st.header('Single Ticker Analysis')
	single_loader(scope, 'single')
	st.markdown("""---""")
	
	ticker = scope.selected['single']['ticker_list'][0]
	
	if ticker in list(scope.ticker_data_files.keys()):
		create_chart_df(scope, ticker)	
		view_charts(scope, ticker)
		

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def intraday_analysis(scope):
	st.header('Intra Day Analysis')	
	single_loader(scope, 'intraday')
	st.markdown("""---""")

	ticker = scope.selected['intraday']['ticker_list'][0]

	if ticker in list(scope.ticker_data_files.keys()):
		# col1,col2 = st.columns([2, 10])
		# df_row_limit = None if scope.analysis_apply_limit=='False' else int(scope.analysis_row_limit)

		print('We are here')
		# share_data = analysis_df(scope, ticker, df_row_limit)  # this only gets refreshed if the ticker changes or the no of rows changes

		
		# Financial Chart adds the following
		# Index(['date', 'open', 'high', 'low', 'close', 'volume', 'MA20', 'MA5'], dtype='object')

		# financial_chart_tutorial(share_data)

		# plot_candlestick_seperate_volume(share_data)

	# 	plot_candlestick(share_data)
		
	# 	plot_line_chart(share_data)


def volume_analysis(scope):
	st.title('Predict Closing Volume to End of Today')
	st.write('Extrapolating the Current Volume to the End of today')
	single_loader(scope, 'volume' )
	st.markdown("""---""")
	ticker = scope.selected['volume']['ticker_list'][0]

	if ticker != 'select a ticker':	
		volume_prediction(scope)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Company Research
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def research_analysis(scope):
	st.header('Company Research')
	single_loader(scope, 'research' )
	st.markdown("""---""")
	
	ticker = scope.selected['research']['ticker_list'][0]

	if ticker != 'select a ticker':	
		view_research_page(ticker)
		


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mult Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def multi_tickers_analysis(scope):
	st.header('Analysis - Multiple Tickers')

	multi_loader(scope)

	view_multi_criteria(scope)

	st.info('I expect the output of any analysis is going to be a list of stocks for further analysis')

	# we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!

	# if len(scope.selected['ticker_list']) > 0:
	# 	st.info('We have some tickers')
	# else:
	# 	st.error('Add some tickers')




