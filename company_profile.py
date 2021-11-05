
import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt
import plotly.graph_objects as go

from share_data import render_share_data_fetcher



def render_company_profile_page(scope):
	st.title('Company Profile')
	# st.write('Just ripping off someone elses code here for the minute')

	ticker = render_select_ticker_for_company(scope)
	st.markdown("""---""")

	if ticker != 'select a ticker':	
		meta_data, info = fetch_yfinance_metadata_for_company_profile(ticker)

		render_company_general_info(info)
		# render_business_summary(info)
		render_fundamental_info(info)

		st.subheader('General meta_data Info') 
		st.markdown('** Market **: ' + info['market'])
		st.markdown('** Exchange **: ' + info['exchange'])
		st.markdown('** Quote Type **: ' + info['quoteType'])

		# lets use our own data and compare
		if ticker in list(scope.share_data_files.keys()):

			# print ( scope.share_data_files.keys() )


			share_data = scope.share_data_files[ticker]
			fig = go.Figure(
					data=go.Scatter(x=share_data['date'], y=share_data['close'])
				)
			fig.update_layout(
				title={
					'text': "Stock Prices Over Past ??????? Years",
					'y':0.9,
					'x':0.5,
					'xanchor': 'center',
					'yanchor': 'top'})
			st.plotly_chart(fig, use_container_width=True)

			# start = dt.datetime.today()-dt.timedelta(2 * 365)
			# end = dt.datetime.today()
			# df = yf.download(ticker,start,end)
			# df = df.reset_index()
			# fig = go.Figure(
			# 		data=go.Scatter(x=df['Date'], y=df['Adj Close'])
			# 	)
			# fig.update_layout(
			# 	title={
			# 		'text': "Stock Prices Over Past Two Years",
			# 		'y':0.9,
			# 		'x':0.5,
			# 		'xanchor': 'center',
			# 		'yanchor': 'top'})
			# st.plotly_chart(fig, use_container_width=True)

			marketInfo = {
					"Volume": info['volume'],
					"Average Volume": info['averageVolume'],
					"Market Cap": info["marketCap"],
					"Float Shares": info['floatShares'],
					"Regular Market Price (USD)": info['regularMarketPrice'],
					'Bid Size': info['bidSize'],
					'Ask Size': info['askSize'],
					"Share Short": info['sharesShort'],
					'Short Ratio': info['shortRatio'],
					'Share Outstanding': info['sharesOutstanding']
				}

			marketDF = pd.DataFrame(data=marketInfo, index=[0])
			st.table(marketDF)
		else:
			st.error( (ticker + ' data has not yet been loaded. Please load some share data so it can be plotted.'))
			render_share_data_fetcher(scope, ticker)
			
			# col1,col2 = st.columns([4,4])
			# # with col1: st.write(('number of Files to Load = ( ' + str((len(scope.tickers_for_multi))) + ' )'))
			# with col1: load_tickers = st.button('Load Share Data File')
			# with col2: st.download_days = st.number_input('change ( - / + )  number of days to download', min_value=1, max_value=1000, value=1, key='0')    
			# with col2: download_tickers = st.button('Download OHLCV Data')
		

		
	else:
		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
		st.error('I dont know if we have any ticker loaded or not!!')




		





# -----------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------
@st.cache
def fetch_yfinance_metadata_for_company_profile(ticker):
	metadata = yf.Ticker(ticker)
	info = metadata.info 
	return metadata, info

def render_select_ticker_for_company(scope):
	col1,col2 = st.columns([2,10])														# col2 is just a dummy to prevent the widget filling the whole screen
	
	dropdown_list = scope.dropdown_ticker_for_company_profile
	index_of_ticker = dropdown_list.index(scope.ticker_for_company_profile)

	with col1: 
		ticker = st.selectbox ( 'Select Ticker', 
								dropdown_list, 
								index=index_of_ticker, 
								help='Select a ticker. Start typing to jump within list'
								) 
	
	scope.ticker_for_company_profile = ticker									# Store the selection for next session
	
	if ticker != 'select a ticker':	
		st.header( scope.ticker_index_file.loc[ticker]['company_name'] )					# Render the company name
		with col2: st.write('button') 
	return ticker

def render_company_general_info(info):
	col1,col2 = st.columns([3,9])
	with col1: st.markdown('** Sector **: ' + info['sector'])
	with col1: st.markdown('** Industry **: ' + info['industry'])
	with col1: st.markdown('** Phone **: ' + info['phone'])
	with col1: st.markdown('** Address **: ' + info['address1'] + ', ' + info['city'] + ', ' + info['zip'] + ', '  +  info['country'])
	with col1: st.markdown('** Website **: ' + info['website'])
	with col2: st.markdown('** Business Summary **')
	# paragraph = info['longBusinessSummary']
	sentences = info['longBusinessSummary'].split('. ')
	for sentence in sentences:
		with col2: st.write(sentence)

def render_2_columns( description, variable ):
	col1,col2,col3 = st.columns([2,2,8])
	with col1: st.write(description)
	with col2: st.write(variable)

def render_fundamental_info(info):
	st.markdown("""---""")
	st.subheader('Fundamental Info') 
		
	render_2_columns( 'Enterprise Value (AUD)', info['enterpriseValue'])
	render_2_columns( 'Enterprise To Revenue Ratio', info['enterpriseToRevenue'])
	render_2_columns( 'Enterprise To Ebitda Ratio', info['enterpriseToEbitda'])
	render_2_columns( 'Net Income (AUD)', info['netIncomeToCommon'])
	render_2_columns( 'Profit Margin Ratio', info['profitMargins'])
	render_2_columns( 'Forward PE Ratio', info['forwardPE'])
	render_2_columns( 'PEG Ratio', info['pegRatio'])
	render_2_columns( 'Price to Book Ratio', info['priceToBook'])
	render_2_columns( 'Forward EPS (AUD)', info['forwardEps'])
	render_2_columns( 'Beta', info['beta'])
	render_2_columns( 'Book Value (AUD)', info['bookValue'])
	render_2_columns( 'Dividend Rate (%)', info['dividendRate'])
	render_2_columns( 'Dividend Yield (%)', info['dividendYield'])
	render_2_columns( 'Five year Avg Dividend Yield (%)', info['fiveYearAvgDividendYield'])
	render_2_columns( 'Payout Ratio', info['payoutRatio'])







# we want to be able to 