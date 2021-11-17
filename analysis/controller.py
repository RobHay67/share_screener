



import streamlit as st


from ticker.loaders.single_loader import single_loader
from ticker.loaders.multi_loader import multi_loader

# from analysis.volume.controller import volume_page
from analysis.volume.controller import volume_prediction
from analysis.research.controller import view_research_page

from analysis.charts.controller import render_selected_charts

from analysis.charts.finance import financial_chart_tutorial
from analysis.charts.candlestick import plot_candlestick_seperate_volume, plot_candlestick
from analysis.charts.line import plot_line_chart



# scope.selected={											# TODO - refactor to "selected"
# 	'multi'		:{'analysis_df':{}, 'ticker_list':[], 				'market':'select entire market', 'industries':None, 'tickers':None  },
# 	'single'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
# 	'intraday'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
# 	'volume'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
# 	'research'	:{'analysis_df':{}, 'ticker_list':['select a ticker']},
# 	}

# ==============================================================================================================================================================
# Single Ticker Analysis
# ==============================================================================================================================================================
def single_ticker_page(scope):
	st.header('Single Ticker Analysis')
	single_loader(scope, 'single')
	st.markdown("""---""")
	
	# print ('ticker list in scope = ', scope.selected['ticker_list'])
	ticker = scope.selected['single']['ticker_list'][0]
	
	if ticker in list(scope.ticker_data_files.keys()):
		
		st.error('We need to add the columns as dictated by the chart we have selected')
		st.error('We will also need to have the indicator setting stored somewhere')

		# TODO - this might be the place to add measures - but only if the have not already been add
		# so - we might collect the measures from the screen.....
		# add the measures to a list and pass the list to a cached function that is responsible
		# 	a) adding any new measures
		# 	b) deleted any removed measures
		# ????? should we record the selected measures if we change screen --- maybe the widgets will keep it 
		# view_alternative_indicators(scope)


		# add_indicators_to_analysis_df(scope, ticker, sma )
# 





		render_selected_charts(scope, ticker)
		# indicator_selectors(scope)
		
		# Financial Chart adds the following
		# Index(['date', 'open', 'high', 'low', 'close', 'volume', 'MA20', 'MA5'], dtype='object')
		# print( scope.ticker_data_files['CBA.AX'])
		# share_data = scope.selected['single']['analysis_df'][ticker]
		# financial_chart_tutorial(scope, ticker)


# ==============================================================================================================================================================
# Intra Day Analysis
# ==============================================================================================================================================================
# TODO - this will need to be moved later
from analysis.intra_day.intraday import add_sma
from analysis.intra_day.intraday import indicator_selectors, alternative_indicators
def intraday_page(scope):
	st.header('Intra Day Analysis')
	
	single_loader(scope, 'intraday')
	
	st.markdown("""---""")

	ticker = scope.selected['intraday']['ticker_list'][0]


	if ticker in list(scope.ticker_data_files.keys()):
		# col1,col2 = st.columns([2, 10])
		# df_row_limit = None if scope.analysis_apply_limit=='False' else int(scope.analysis_row_limit)

		print('We are here')
		# share_data = analysis_df(scope, ticker, df_row_limit)  # this only gets refreshed if the ticker changes or the no of rows changes

		# TODO - this might be the place to add measures - but only if the have not already been added
		# so - we might collect the measures from the screen.....
		# add the measures to a list and pass the list to a cached function that is responsible
		# 	a) adding any new measures
		# 	b) deleted any removed measures
		# ????? should we record the selected measures if we change screen --- maybe the widgets will keep it 
		# view_alternative_indicators(scope)


		# indicator_selectors(scope)
		
		# Financial Chart adds the following
		# Index(['date', 'open', 'high', 'low', 'close', 'volume', 'MA20', 'MA5'], dtype='object')

		# financial_chart_tutorial(share_data)

		# plot_candlestick_seperate_volume(share_data)

	# 	plot_candlestick(share_data)
		
	# 	plot_line_chart(share_data)


def volume_page(scope):
	st.title('Predict Closing Volume to End of Today')
	st.write('Extrapolating the Current Volume to the End of today')
	single_loader(scope, 'volume' )
	st.markdown("""---""")
	ticker = scope.selected['volume']['ticker_list'][0]

	if ticker != 'select a ticker':	
		volume_prediction(scope)

# ==============================================================================================================================================================
# Company Research
# ==============================================================================================================================================================
def research_page(scope):
	st.header('Company Research')
	single_loader(scope, 'research' )
	st.markdown("""---""")
	
	ticker = scope.selected['research']['ticker_list'][0]

	if ticker != 'select a ticker':	
		view_research_page(ticker)
		


# ==============================================================================================================================================================
# Mult Ticker Analysis
# ==============================================================================================================================================================
def multi_tickers_page(scope):
	st.header('Analysis - Multiple Tickers')

	multi_loader(scope)

	st.info('I expect the output of any analysis is going to be a list of stocks for further analysis')

	# we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!

	# if len(scope.selected['ticker_list']) > 0:
	# 	st.info('We have some tickers')
	# else:
	# 	st.error('Add some tickers')






# col1,col2,col3,col4,col5,col6,col7,col8 = st.columns(8)
# with col1: st.write('Select Options')
# Options for the chart
# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: left;}</style>', unsafe_allow_html=True)
# with col2: show_weekends 	= st.radio("weekends", ('Hide','Show'), key=1)
# with col3: show_volume 		= st.radio("volume"  , ('Hide','Show'), key=2)

# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: left;}</style>', unsafe_allow_html=True)
# with col1: st.checkbox('CandleStick', value=True, key='1')
# with col2: st.checkbox('Line', key='2')



# col1,col2 = st.columns([2, 10])