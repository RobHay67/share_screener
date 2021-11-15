
import streamlit as st
import pandas as pd

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Company Research Page Sections
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def dividends(dividends):
	st.markdown('##### Dividends') 
	dividends = pd.DataFrame(dividends)
	dividends.reset_index(inplace=True)
	dividends.sort_values(by=['Date'], inplace=True, ascending=False)
	my_expander = st.expander(label='Dividends')
	my_expander.dataframe(dividends, 2000, 2000)

def company_general(info):
	col1,col2 = st.columns([3,9])
	with col1: st.markdown('** Sector **: ' + info['sector'])
	with col1: st.markdown('** Industry **: ' + info['industry'])
	# with col1: st.markdown('** Phone **: ' + info['phone'])
	# with col1: st.markdown('** Address **: ' + info['address1'] + ', ' + info['city'] + ', ' + info['zip'] + ', '  +  info['country'])
	with col1: st.markdown('** Website **: ' + info['website'])
	with col2: st.markdown('** Business Summary **')
	# paragraph = info['longBusinessSummary']
	sentences = info['longBusinessSummary'].split('. ')
	for sentence in sentences:
		with col2: st.write(sentence)

def fundamental(info):
	st.markdown('##### Fundamental Info') 
		
	view_2_columns( 'Enterprise Value (AUD)', info['enterpriseValue'])
	view_2_columns( 'Enterprise To Revenue Ratio', info['enterpriseToRevenue'])
	view_2_columns( 'Enterprise To Ebitda Ratio', info['enterpriseToEbitda'])
	view_2_columns( 'Net Income (AUD)', info['netIncomeToCommon'])
	view_2_columns( 'Profit Margin Ratio', info['profitMargins'])
	view_2_columns( 'Forward PE Ratio', info['forwardPE'])
	view_2_columns( 'PEG Ratio', info['pegRatio'])
	view_2_columns( 'Price to Book Ratio', info['priceToBook'])
	view_2_columns( 'Forward EPS (AUD)', info['forwardEps'])
	view_2_columns( 'Beta', info['beta'])
	view_2_columns( 'Book Value (AUD)', info['bookValue'])
	view_2_columns( 'Dividend Rate (%)', info['dividendRate'])
	view_2_columns( 'Dividend Yield (%)', info['dividendYield'])
	view_2_columns( 'Five year Avg Dividend Yield (%)', info['fiveYearAvgDividendYield'])
	view_2_columns( 'Payout Ratio', info['payoutRatio'])

def general(info):
	st.markdown('##### General meta_data Info') 
	st.markdown('** Market **: ' + info['market'])
	st.markdown('** Exchange **: ' + info['exchange'])
	st.markdown('** Quote Type **: ' + info['quoteType'])

def plot_basic_chart(scope):
	import plotly.graph_objects as go
	st.markdown('##### Chart of all available data') 

	ticker = scope.selected['research']['ticker_list'][0]

	if ticker in list(scope.ticker_data_files.keys()):
		share_data = scope.ticker_data_files[ticker]
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
		st.warning('ROB to change chart to candlestick and maybe add a widget for the date range')
	else:
		st.error('Load and/or Download Share Data to see the chart')

def market_info(info):
	st.markdown('##### Market Information') 
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

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# helpers
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_2_columns( description, variable ):
	col1,col2,col3 = st.columns([2,2,8])
	with col1: st.write(description)
	with col2: st.write(variable)




