
import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt
import plotly.graph_objects as go

def render_company_profile_page(scope):
	st.title('Company Profile')

	# st.title('Analysis Page')

	st.write('Just ripping off someone elses code here for the minute')
	ticker = scope.ticker_list[0]
	stock = yf.Ticker(ticker)
	info = stock.info 

	st.markdown("""---""")
	
	st.header(info['longName']) 
	st.subheader(ticker)

	# if len(scope.ticker_list) > 0:
	# 	ticker_1 = scope.ticker_list[0]
	# 	if len(scope.ticker_list) > 1:
	# 		st.error( 'Ticker List contains more that 1 ticker. Analysis to be performed on the first ticker only > ' + ticker_1)


	st.markdown('** Sector **: ' + info['sector'])
	st.markdown('** Industry **: ' + info['industry'])
	st.markdown('** Phone **: ' + info['phone'])
	st.markdown('** Address **: ' + info['address1'] + ', ' + info['city'] + ', ' + info['zip'] + ', '  +  info['country'])
	st.markdown('** Website **: ' + info['website'])
	st.markdown('** Business Summary **')
	st.info(info['longBusinessSummary'])

	fundInfo = {
			'Enterprise Value (AUD)': info['enterpriseValue'],
			'Enterprise To Revenue Ratio': info['enterpriseToRevenue'],
			'Enterprise To Ebitda Ratio': info['enterpriseToEbitda'],
			'Net Income (AUD)': info['netIncomeToCommon'],
			'Profit Margin Ratio': info['profitMargins'],
			'Forward PE Ratio': info['forwardPE'],
			'PEG Ratio': info['pegRatio'],
			'Price to Book Ratio': info['priceToBook'],
			'Forward EPS (AUD)': info['forwardEps'],
			'Beta ': info['beta'],
			'Book Value (AUD)': info['bookValue'],
			'Dividend Rate (%)': info['dividendRate'], 
			'Dividend Yield (%)': info['dividendYield'],
			'Five year Avg Dividend Yield (%)': info['fiveYearAvgDividendYield'],
			'Payout Ratio': info['payoutRatio']
		}
	
	fundDF = pd.DataFrame.from_dict(fundInfo, orient='index')
	fundDF = fundDF.rename(columns={0: 'Value'})
	st.subheader('Fundamental Info') 
	st.table(fundDF)




	st.subheader('General Stock Info') 
	st.markdown('** Market **: ' + info['market'])
	st.markdown('** Exchange **: ' + info['exchange'])
	st.markdown('** Quote Type **: ' + info['quoteType'])






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
	else:
		st.error( (ticker + ' data has not yet been loaded. Please load some share data so it can be plotted.'))





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
